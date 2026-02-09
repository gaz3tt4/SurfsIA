import requests
import geocoder
import json

def get_ip_address():
    g = geocoder.ip('me')
    return g.ip

def getLocation(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

ip_address = get_ip_address()
location = getLocation(ip_address)
location = json.dumps(location, indent=4, separators=(',', ': '))
print(location)
