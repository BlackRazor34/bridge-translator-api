# Python image
FROM python:3.11-slim

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizini
WORKDIR /app

# Requirements'ı önce kopyala (cache optimizasyonu için)
COPY requirements.txt .

# Bağımlılıkları yükle
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyasını kopyala
COPY app.py .

# Port'u expose et
EXPOSE 8500

# Uygulamayı başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8500"]