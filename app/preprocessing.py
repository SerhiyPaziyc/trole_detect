# app/preprocessing.py

import re
import string

class TextPreprocessor:
    def __init__(self):
        pass

    def clean_text(self, text):
        """Очищає текст: видаляє непотрібні символи та приводить до нижнього регістру"""
        text = text.lower()  # Переведення в нижній регістр
        text = re.sub(r'http\S+', '', text)  # Видалення URL-адрес
        text = re.sub(r'@\S+', '', text)  # Видалення згадок користувачів
        text = re.sub(r'\d+', '', text)  # Видалення цифр
        text = text.translate(str.maketrans('', '', string.punctuation))  # Видалення пунктуації
        return text
