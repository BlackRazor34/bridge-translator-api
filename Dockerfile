# Python image
FROM python:3.11-slim

# Çalışma dizini
WORKDIR /app

# Requirements'ı önce kopyala (cache optimizasyonu için)
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ÖNEMLİ DEĞİŞİKLİK:
# Geri kalan tüm proje dosyalarını (app.py, static/, templates/) kopyala
COPY . .

# Port'u expose et
EXPOSE 8500

# Uygulamayı başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8500"]