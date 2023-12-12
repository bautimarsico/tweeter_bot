
import datetime
import requests
import emoji
from googletrans import Translator


translator = Translator()

def kelvin_to_celsius(int):
    int = round(int -273.85, 2)
    return int

key = "a6b7bd1101bda6a77402c916b0fa7067"
r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-34.583333&lon=-58.333333&appid=a6b7bd1101bda6a77402c916b0fa7067")




date = datetime.datetime.now().strftime("%d/%m/%Y")


description = r.json()["weather"][0]["description"]
description = translator.translate( description , dest = 'es')
description = description.text

max_temp = float(r.json()["main"]["temp_max"])

min_temp = float(r.json()["main"]["temp_min"])

feels_like = kelvin_to_celsius(float(r.json()["main"]["feels_like"]))

pressure = r.json()["main"]["pressure"]

humidity = r.json()["main"]["humidity"]


tweet = f'''El clima en CABA el {date} es el siguiente:
descripción: {description} :globe_showing_Americas:
sensación termica: {feels_like}°C :thermometer:
humedad: {humidity} % :droplet:
 '''


#print(datetime.datetime.now().minute)

