from fastapi import FastAPI, Query, HTTPException
from transformers import MarianMTModel, MarianTokenizer
import logging

# Logging ayarla
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="English to Turkish Translator")

# Model yükleme
model_name = "Helsinki-NLP/opus-mt-tc-big-en-tr"

try:
    logger.info(f"Loading tokenizer: {model_name}")
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    logger.info(f"Loading model: {model_name}")
    model = MarianMTModel.from_pretrained(model_name)
    
    logger.info("Model and tokenizer loaded successfully!")
    
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise e

@app.get("/")
def read_root():
    return {"message": "Welcome to English to Turkish Translator API"}

@app.get("/translate")
def translate(q: str = Query(..., description="Text to translate from English to Turkish")):
    try:
        if not q.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        inputs = tokenizer([q], return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        result = tokenizer.decode(translated[0], skip_special_tokens=True)
        
        return {"original": q, "translation": result}
    
    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=500, detail="Translation failed")

@app.get("/health")
def health_check():
    return {"status": "healthy", "model": model_name}