import getInformation
import getLoc
import agent    

def main():
    
    ip_address = getLoc.get_ip_address()
    
    location = getLoc.getLocation(ip_address)


    lat = location['lat']
    lng = location['lon']
    information = getInformation.getStormData(lat, lng)
    information_return = agent.process(information)
    print(information_return)
