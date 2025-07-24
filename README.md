# English to Turkish Translator API EN➡️TR

This project provides a REST API for translating English text to Turkish using the `Helsinki-NLP/opus-mt-tc-big-en-tr` model.

## 🚀 Run with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t engintranslator .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8500 engintranslator
    ```
    (We map port 8000 on our local machine to port 8500 inside the container)

## 🧪 Example

Open your browser or use curl for the following URL. Note that the query parameter is `q`.