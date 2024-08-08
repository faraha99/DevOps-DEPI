"""
Flask application to display weather information based on selected country.
"""

from datetime import datetime, timedelta
import requests
import pytz
from flask import Flask, request, render_template

app = Flask(__name__)

# Hardcoded API_KEY for testing purposes
API_KEY = 'bad4c8cff47886ca6d92626fbee32d8e'

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

def get_weather(city: str) -> dict:
    """
    Fetches weather data for a given city.
    """
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={API_KEY}&units=metric"
    )
    response = requests.get(url, timeout=10)
    weather_data = response.json()
    print(weather_data)  # Print the full response for debugging
    return weather_data

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the index page and handles form submissions.
    """
    if request.method == 'POST':
        country = request.form['country']
        city = COUNTRIES.get(country)
        if city:
            weather_data = get_weather(city)
            country_code = next(
                (code for code, name in pytz.country_names.items() if name == country),
                None
            )
            if country_code:
                time_zone = pytz.timezone(pytz.country_timezones[country_code][0])
                current_time = datetime.now(time_zone)
                adjusted_time = current_time - timedelta(hours=1)
                
                # Extract weather data safely
                weather_description = weather_data.get('weather', [{}])[0].get(
                    'description', 'No description available'
                )
                temperature = weather_data.get('main', {}).get(
                    'temp', 'Temperature data not available'
                )
                
                data = {
                    'country': country,
                    'city': city,
                    'current_time': adjusted_time.strftime('%Y-%m-%d %I:%M:%S %p'),
                    'time_zone': time_zone.zone,
                    'weather': {
                        'description': weather_description,
                        'temperature': temperature
                    }
                }
                return render_template('index.html', data=data, countries=COUNTRIES.keys())
    return render_template('index.html', countries=COUNTRIES.keys())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
