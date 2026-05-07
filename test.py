import requests
import json
city = "Indianapolis"
country = "US"
api_key = "edc9763b43e65662faa4ed8a50cf6537"
weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
weather_data = weather_url.json()
temp = round(weather_data['main']['temp'])
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']