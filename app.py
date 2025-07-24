from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import MarianMTModel, MarianTokenizer
import logging

# Logging ayarları
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI Uygulaması
app = FastAPI(title="Bridge: EN <> TR Translator API")

# Statik dosyaları (CSS) sunmak için mount et
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML şablonlarını sunmak için templates dizinini ayarla
templates = Jinja2Templates(directory="templates")

# Model yükleme
model_name = "Helsinki-NLP/opus-mt-tc-big-en-tr"

try:
    logger.info(f"Tokenizer yükleniyor: {model_name}")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    logger.info(f"Model yükleniyor: {model_name}")
    model = MarianMTModel.from_pretrained(model_name)
    
    logger.info("Model ve tokenizer başarıyla yüklendi!")
    
except Exception as e:
    logger.error(f"Model yüklenirken hata oluştu: {str(e)}")
    raise e

# Ana sayfa endpoint'i - HTML arayüzünü sunar
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Çeviri endpoint'i - JavaScript tarafından çağrılır
@app.get("/translate")
def translate(q: str = Query(..., description="İngilizce'den Türkçe'ye çevrilecek metin")):
    try:
        if not q.strip():
            raise HTTPException(status_code=400, detail="Metin boş olamaz")
        
        inputs = tokenizer([q], return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        result = tokenizer.decode(translated[0], skip_special_tokens=True)
        
        return {"original": q, "translation": result}
    
    except Exception as e:
        logger.error(f"Çeviri hatası: {str(e)}")
        raise HTTPException(status_code=500, detail="Çeviri işlemi başarısız oldu")

# Sağlık kontrolü endpoint'i
@app.get("/health")
def health_check():
    return {"status": "healthy", "model": model_name}