from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST', 'BACK', 'INTERPRET'])
def index():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "###"
        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
        weather_data = weather_url.json()
        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)
    if request.method == "BACK":
        return render_template("index.html")
    if request.method == "INTERPRET":
        return render_template("interpretations.html")
    user_name = "Mustafa"
    return render_template("index.html", user_name=user_name)

@app.route('/testing')
def name():
    user_name = "Testing"
    return render_template("testing.html", user_name=user_name)

if __name__ == '__main__':
    app.run(port=5000, debug=True)


city="Indianapolis"
country = "US"
weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
weather_data = weather_url.json()
temp = round(weather_data['main']['_temp_'])
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']