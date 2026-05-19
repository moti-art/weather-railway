from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None

    if request.method == 'POST':
        city_key = request.form.get('city')
        try:
            response = requests.get(f"{BACKEND_URL}/weather/{city_key}")
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error = f"Error: Backend returned status {response.status_code}"
        except Exception as e:
            error = f"Could not connect to Backend at {BACKEND_URL}. Error: {e}"

    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
