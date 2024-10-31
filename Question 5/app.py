from flask import Flask, request, render_template
import random

app = Flask(__name__)
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Don't limit your challenges. Challenge your limits.",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Dream big and dare to fail. - Norman Vaughan",
    "If you want something you've never had, you must be willing to do something you've never done.",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote', methods=['GET'])
def quote():
    return render_template('quote.html', quote=random.choice(quotes))

if __name__ == '__main__':
    app.run(debug=True)