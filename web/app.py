# web/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from app.hate_detector import HateDetector
from app.troll_identifier import TrollIdentifier
from app.preprocessing import TextPreprocessor

app = Flask(__name__)

# Ініціалізація компонентів
hate_detector = HateDetector()
troll_identifier = TrollIdentifier()
preprocessor = TextPreprocessor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    cleaned_text = preprocessor.clean_text(text)
    
    toxicity = hate_detector.analyze_text(cleaned_text)
    is_troll = troll_identifier.identify_troll({'message_count': random.randint(1, 100)})  # Тестова активність
    
    return render_template('result.html', toxicity=toxicity, is_troll=is_troll)

if __name__ == '__main__':
    app.run(debug=True)
