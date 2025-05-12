import requests

URL = "https://restcountries.com/v3.1/currency/KES"

def get_country_data():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(URL, headers=headers)
    return response
