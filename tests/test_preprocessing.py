# tests/test_preprocessing.py

import unittest
from app.preprocessing import TextPreprocessor

class TestTextPreprocessor(unittest.TestCase):

    def setUp(self):
        self.preprocessor = TextPreprocessor()

    def test_clean_text(self):
        input_text = "Hello @user, visit http://example.com for more details!"
        expected_output = "hello visit for more details"
        cleaned_text = self.preprocessor.clean_text(input_text)
        self.assertEqual(cleaned_text, expected_output)

if __name__ == '__main__':
    unittest.main()
