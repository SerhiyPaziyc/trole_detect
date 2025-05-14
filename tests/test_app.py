# tests/test_app.py

import unittest
from web.app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_analyze_page(self):
        response = self.app.post('/analyze', data={'text': 'You are a great person!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Toxicity:', response.data)

if __name__ == '__main__':
    unittest.main()
