'''
This module fetches information from weather api
'''
import requests

# Construct the URL for current conditions
def get_url():
    '''
    fetches weather information

    Return:
        response: The weather information
    '''
    url = 'https://api.open-meteo.com/v1/forecast?latitude=6.6885&longitude=-1.6244&current_weather=true'
    response = requests.get(url)
    return response