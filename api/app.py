import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests
import json
load_dotenv()

app = Flask(__name__)
api_key = os.getenv("api_key")

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = os.getenv("api_key")
        error = None
        if not city:
            error = "Enter a city."
        if not country:
            error = "Enter a country."
        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
        if weather_url.status_code == 404:
            return render_template(
                "index.html",
                error="Invalid city or country, try again."
            )
        if weather_url.status_code != 200:
            return render_template(
                "index.html",
                error="Internal error. Make sure to input a city and country or try again later."
            )
        weather_data = weather_url.json()
        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, error=error)
    if request.method == "GET":
        return render_template("index.html")
    user_name = "Mustafa"
    return render_template("index.html", user_name=user_name)

@app.route('/testing')
def name():
    user_name = "Testing"
    return render_template("testing.html", user_name=user_name)

if __name__ == '__main__':
    app.run(port=5000, debug=True)