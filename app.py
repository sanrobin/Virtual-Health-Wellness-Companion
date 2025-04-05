from flask import Flask, render_template, request, jsonify
import random
import requests
from datetime import datetime

app = Flask(__name__)

# Sample wellness tips
WELLNESS_TIPS = [
    "Drink at least 8 glasses of water daily",
    "Take a 10-minute walk break every 2 hours",
    "Practice deep breathing exercises",
    "Get 7-8 hours of sleep each night",
    "Include colorful vegetables in your meals"
]

# Sample motivational quotes
MOTIVATIONAL_QUOTES = [
    "The only bad workout is the one that didn't happen.",
    "Take care of your body. It's the only place you have to live.",
    "Your health is an investment, not an expense.",
    "Small steps lead to big changes.",
    "Wellness is a journey, not a destination."
]

# Simple in-memory storage for diet tracking
diet_logs = []

@app.route('/')
def home():
    # Get daily tip and quote
    daily_tip = random.choice(WELLNESS_TIPS)
    daily_quote = random.choice(MOTIVATIONAL_QUOTES)
    
    # Try to fetch a quote from an external API
    try:
        response = requests.get('https://api.quotable.io/random')
        if response.status_code == 200:
            daily_quote = response.json()['content']
    except:
        pass  # Fallback to local quotes if API fails
    
    return render_template('index.html', tip=daily_tip, quote=daily_quote, diet_logs=diet_logs)

@app.route('/add_meal', methods=['POST'])
def add_meal():
    meal_data = {
        'meal': request.form.get('meal'),
        'description': request.form.get('description'),
        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    diet_logs.insert(0, meal_data)  # Add to beginning of list
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)