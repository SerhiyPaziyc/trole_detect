# Використовуємо Python 3.12 як базовий образ
FROM python:3.12-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли в контейнер
COPY . .

# Встановлюємо всі залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт 5000 для веб-додатку
EXPOSE 5000

# Запускаємо Flask додаток
CMD ["python", "web/app.py"]
