import requests 
import json 
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.stormglass.io/v2/marine/point'



def getStormData(lat, lng):
    response = requests.get(
        url ,
        params={
            'lat': lat,
            'lng': lng,
            'params': 'windSpeed',
        },
        headers={
            'Authorization': 'STORM_KEY'
        }
    )

    json_data = response.json()
    return json_data