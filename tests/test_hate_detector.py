# tests/test_hate_detector.py

import unittest
from app.hate_detector import HateDetector

class TestHateDetector(unittest.TestCase):

    def setUp(self):
        self.hate_detector = HateDetector()

    def test_analyze_text(self):
        # Приклад тексту з високою токсичністю
        text = "You are a horrible person!"
        result = self.hate_detector.analyze_text(text)
        self.assertGreater(result['toxicity'], 0.5)

        # Текст без токсичності
        text = "Hello, how are you?"
        result = self.hate_detector.analyze_text(text)
        self.assertLess(result['toxicity'], 0.5)

if __name__ == '__main__':
    unittest.main()
