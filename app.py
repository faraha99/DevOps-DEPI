from flask import Flask, request, render_template
import requests
import pytz
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Fetch API_KEY from environment variables
API_KEY = os.getenv('API_KEY')

COUNTRIES = {
    'Egypt': 'Cairo',
    'India': 'Delhi',
    'Japan': 'Tokyo',
    'Brazil': 'Sao Paulo',
    'Australia': 'Sydney',
    'France': 'Paris',
    'Canada': 'Toronto',
    'Germany': 'Berlin',
    'South Africa': 'Cape Town'
}

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)  # Timeout set to 10 seconds (adjust as needed)
    weather_data = response.json()
    return weather_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']
        city = COUNTRIES.get(country)
        if city:
            weather_data = get_weather(city)
            country_code = next((code for code, name in pytz.country_names.items() if name == country), None)
            if country_code:
                time_zone = pytz.timezone(pytz.country_timezones[country_code][0])
                current_time = datetime.now(time_zone)
                adjusted_time = current_time - timedelta(hours=1)
                data = {
                    'country': country,
                    'city': city,
                    'current_time': adjusted_time.strftime('%Y-%m-%d %I:%M:%S %p'),
                    'time_zone': time_zone.zone,
                    'weather': {
                        'description': weather_data['weather'][0]['description'],
                        'temperature': weather_data['main']['temp']
                    }
                }
                return render_template('index.html', data=data, countries=COUNTRIES.keys())
    return render_template('index.html', countries=COUNTRIES.keys())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

