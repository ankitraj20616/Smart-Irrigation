import requests
from GPS import FindCurrentLocation
class  FindCurrentWeather : 

    def detectWeather(self):
        gps = FindCurrentLocation()
        current_location = gps.locationCordinates()
        city = current_location.get('city', 'Unknown')
        state = current_location.get('state', 'Unknown')
        api_key = '35e3a8dce689acc944efa3ebd0ee84bb'
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state}&APPID={api_key}'
        
        api_response = requests.get(api_url)
        print(api_response.json())
    

    
    

if __name__ == "__main__":
    weatherDetector = FindCurrentWeather()
    weatherDetector.detectWeather()