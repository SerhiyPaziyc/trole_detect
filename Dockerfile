FROM python:3.12-slim

# Встановлюємо git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Робоча директорія
WORKDIR /app

# Копіюємо файли
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо порт
EXPOSE 5000

# Команда для запуску Flask
CMD ["python", "web/app.py"]
