# app/hate_detector.py

from detoxify import Detoxify

class HateDetector:
    def __init__(self):
        self.model = Detoxify('original')  # Завантаження попередньо навченої моделі

    def analyze_text(self, text):
        """Аналізує текст і повертає оцінки токсичності"""
        return self.model.predict(text)

    def is_toxic(self, text, threshold=0.7):
        """Перевіряє, чи є текст токсичним, порівнюючи результат з пороговим значенням"""
        result = self.analyze_text(text)
        return result['toxicity'] >= threshold
