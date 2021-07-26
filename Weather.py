from typing import MutableMapping
import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
lon=((api_data['coord']['lon']))
lat=((api_data['coord']['lat']))
sunrise=((api_data["sys"]["sunrise"])/100000000)
sunset=((api_data["sys"]["sunset"])/100000000)
temp_min=((api_data["main"]["temp_min"])- 273.15)
temp_max=((api_data["main"]['temp_max'])- 273.15)
country=((api_data['sys']['country']))

print ("-------------------------------------------------------------")
print ("Location - {}  || {}Lon || {}lat".format(location.upper(),lon, lat ))
print ("Sun range: Sunrise- {:.2f}  || Sunset- {:.2f}".format(sunrise,sunset))
print ("Temperature Range - Max-{:.2f}  || Min-{:.2f} || Avg-{:.2f}".format(temp_min,temp_max,temp_city))
print ("-------------------------------------------------------------")

print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
print ("Country               :", country)
print ("         ",date_time)
print("====================================================")
