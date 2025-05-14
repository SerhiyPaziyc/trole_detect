# app/troll_identifier.py

import random

class TrollIdentifier:
    def __init__(self):
        # Можна додати додаткові моделі або логіку
        pass

    def identify_troll(self, user_activity):
        """Визначає, чи є користувач тролем на основі його активності"""
        # Ось проста евристика: якщо кількість повідомлень користувача більша за певний поріг, то це може бути троль.
        if user_activity['message_count'] > 50:  # Можна змінити поріг за потреби
            return True
        return False
