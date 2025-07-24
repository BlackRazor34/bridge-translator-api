# EN > TR Çeviri API 🇬🇧➡️🇹🇷

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Ready-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

Bu proje, yüksek performanslı **Helsinki-NLP** yapay zeka modelini kullanarak İngilizce metinleri anında Türkçe'ye çeviren modern bir REST API sunar. FastAPI altyapısı üzerine kurulmuştur ve Docker ile saniyeler içinde çalıştırılabilir.

## ✨ Öne Çıkan Özellikler

* **Yüksek Kaliteli Çeviri:** Alanında kanıtlanmış `opus-mt-tc-big-en-tr` modeli ile doğru ve akıcı çeviriler.
* **Yüksek Performans:** Asenkron yapıdaki FastAPI sayesinde hızlı yanıt süreleri.
* **Kolay Kurulum:** Docker desteği ile tek komutla kurulum ve çalıştırma imkanı.
* **İnteraktif Dökümantasyon:** Otomatik oluşturulan Swagger UI (`/docs`) sayfası ile kolay test ve entegrasyon.
* **Sağlık Kontrolü:** Uygulamanın durumunu izlemek için `/health` endpoint'i.

## 🛠️ Teknoloji Mimarisi

Bu projenin arkasındaki temel teknolojiler:

* **FastAPI:** Modern, hızlı ve asenkron web framework'ü.
* **Uvicorn:** FastAPI için yüksek performanslı ASGI sunucusu.
* **Transformers:** Hugging Face'in son teknoloji yapay zeka modellerini kullanmak için geliştirilmiş kütüphanesi.
* **PyTorch:** Modelin çalıştığı temel derin öğrenme platformu.
* **Docker:** Uygulamayı ve bağımlılıklarını izole bir ortamda paketlemek için kullanılan konteyner teknolojisi.

## 🚀 Hızlı Başlangıç (Docker ile)

Projeyi çalıştırmanın en hızlı ve tavsiye edilen yolu Docker kullanmaktır.

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/kullanici-adiniz/proje-adiniz.git](https://github.com/kullanici-adiniz/proje-adiniz.git)
    cd proje-adiniz
    ```
    *(Not: Henüz GitHub'a yüklemediyseniz bu adımı atlayıp doğrudan proje klasörünüzde devam edebilirsiniz.)*

2.  **Docker İmajını Oluşturun (Build):**
    ```bash
    docker build -t eng-tur-translator .
    ```

3.  **Container'ı Çalıştırın (Run):**
    ```bash
    docker run -p 8000:8500 eng-tur-translator
    ```
    Uygulamanız artık `http://localhost:8000` adresinde çalışıyor!

## 🔌 API Endpoint'leri

Aşağıdaki endpoint'ler üzerinden API'ye erişebilirsiniz:

| Metot | Endpoint | Açıklama |
| :--- | :--- | :--- |
| `GET` | `/` | API için basit bir karşılama mesajı döndürür. |
| `GET` | `/translate` | `q` parametresi ile gönderilen İngilizce metni Türkçe'ye çevirir. |
| `GET` | `/docs` | İnteraktif Swagger UI dökümantasyonunu sunar. |
| `GET` | `/health` | API'nin ve modelin sağlık durumunu kontrol eder. |

## 💻 Yerel Geliştirme Ortamı

Projeyi Docker olmadan, kendi bilgisayarınızda çalıştırmak isterseniz:

1.  **Sanal Ortam Oluşturun ve Aktif Edin:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    .\venv\Scripts\activate    # Windows
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Uygulamayı Başlatın:**
    ```bash
    uvicorn app:app --reload
    ```
    Uygulama şimdi `http://127.0.0.1:8000` adresinde çalışacaktır.

## 📄 Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.