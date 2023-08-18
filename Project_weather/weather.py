'''
A program that produces the weather update of Kumasi
'''
import requests
from get_url import get_url

# Make the API request
response = get_url()

if response.status_code == 200:
    weather_data = response.json()['current_weather']
    # Extract and print relevant weather information
    print("Kumasi Current Weather Condition:")
    for key, value in weather_data.items():
        print("\t{} : {}".format(key, value))
else:
    print("Error:", response.status_code)
