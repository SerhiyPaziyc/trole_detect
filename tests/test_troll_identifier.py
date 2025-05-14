# tests/test_troll_identifier.py

import unittest
from app.troll_identifier import TrollIdentifier

class TestTrollIdentifier(unittest.TestCase):

    def setUp(self):
        self.troll_identifier = TrollIdentifier()

    def test_identify_troll(self):
        # Якщо кількість повідомлень більше 50, має бути виявлений троль
        user_activity = {'message_count': 60}
        self.assertTrue(self.troll_identifier.identify_troll(user_activity))
        
        # Якщо менше або рівно 50, не троль
        user_activity = {'message_count': 20}
        self.assertFalse(self.troll_identifier.identify_troll(user_activity))

if __name__ == '__main__':
    unittest.main()
