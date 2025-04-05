# Virtual Health & Wellness Companion

A simple and user-friendly web application that helps users maintain their well-being through daily wellness tips, diet tracking, and motivational quotes.

## Features

- Daily Wellness Tips
- Interactive Diet Tracker
- Motivational Quotes (with external API integration)
- Modern, responsive design
- Simple and intuitive user interface

## Technical Stack

- Backend: Python Flask
- Frontend: HTML, CSS, JavaScript
- External API: quotable.io for dynamic quotes

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd virtual-health-wellness-companion
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. **View Daily Tips and Quotes**: The homepage automatically displays a random wellness tip and motivational quote.

2. **Track Your Diet**:
   - Select a meal type from the dropdown
   - Enter the description of what you ate
   - Click "Add Meal" to save your entry

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Application styles
│   └── js/
│       └── script.js  # Frontend JavaScript
└── templates/
    └── index.html     # Main HTML template
```

## Dependencies

- Flask: Web framework
- Requests: HTTP library for API calls

## Features Details

1. **Daily Wellness Tips**
   - Randomly selected from a curated list
   - Updated on page refresh

2. **Diet Tracker**
   - Simple form interface
   - Chronological display of meals
   - Includes meal type, description, and timestamp

3. **Motivational Quotes**
   - Integration with external API (quotable.io)
   - Fallback to local quotes if API is unavailable

## Contributing

Feel free to submit issues and enhancement requests!
