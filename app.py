import os
from datetime import datetime

import pytz
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

app = Flask(__name__)
load_dotenv('.env')


@app.route('/')
def home():
    # Get current time in Cairo, Egypt
    egypt_tz = pytz.timezone('Africa/Cairo')
    egypt_time = datetime.now(egypt_tz)

    # Format the time as string
    formatted_time = egypt_time.strftime('%Y-%m-%d %H:%M %p')

    # Get weather data for Cairo, Egypt.
    api_key = os.getenv('API_KEY')
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q=Cairo,EG&units=metric&appid={api_key}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Extract weather description and temperature if available
    if 'weather' in weather_data:
        weather_description = weather_data['weather'][0]['description']
    else:
        weather_description = 'Weather data unavailable'

    if 'main' in weather_data:
        temperature = weather_data['main']['temp']
    else:
        temperature = 'Temperature data unavailable'

    return render_template('index.html',
                           current_time=formatted_time,
                           time_zone='Africa/Cairo',
                           weather_description=weather_description,
                           temperature=temperature)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
