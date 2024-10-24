FROM python:3.9

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tokenswave.wsgi"]