'''
A program that produces the weather update of cities in major Cities in Ghana
'''
import requests
from city import cordinates

parameters = {'latitude':cordinates[0], 'longitude': cordinates[1], 'current_weather':'true'}
url = 'https://api.open-meteo.com/v1/forecast'

# Make the API request
response = requests.get(url, params=parameters)

if response.status_code == 200:
    weather_data = response.json()['current_weather']
    # Extract and print relevant weather information
    print("Current Weather Condition:")
    for key, value in weather_data.items():
        print("\t{} : {}".format(key, value))
else:
    print("Error:", response.status_code)
