import requests 
from dotenv import load_dotenv
import json
import os 
import datetime

load_dotenv()


url = 'https://api.stormglass.io/v2/weather/point'

lat = -23.7872
lng = -45.5617

start = datetime.datetime.now()
end = start + datetime.timedelta(days=1)



def getStormData(lat, lng):
    STORM_KEY = os.getenv('STORM_KEY')
    
    response = requests.get(
        url ,
        params={
            'lat': lat,
            'lng': lng,
            'params': ','.join(['swellDirection', 'swellHeight', 'swellPeriod', 'windDirection', 'windSpeed', 'waveHeight', 'wavePeriod']),
            'source': 'noaa',
            'start': start.day,
            'end': end.day
        },
        headers={
            'Authorization': STORM_KEY
        }
    )

    json_data = json.dumps(response.json(), indent=4, separators=(',', ': '))
    return json_data


teste = getStormData(lat, lng)
print(teste)