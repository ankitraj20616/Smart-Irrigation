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
        
        return api_response.json()
        
    def detectRain(self):
        weather_data = self.detectWeather()

        temperature = weather_data['main']['temp'] - 273.15 # Converted Into Celcius 
        humidity = weather_data['main']['humidity']
        weather_description = weather_data['weather'][0]['description']

        if temperature > 30:
            print("Temperature in the surrounding is very high, Water the plant")
            return

        elif humidity < 30:
            print("Humidity is very low, Water the plant")
            return
        
        elif 'rain' not in weather_description or 'thunderstorm' not in weather_description:
            print("Rain is not going to happen now, Water the plant")
            return
        else:
            print("You don't have to Water the plant now.")
        
        

    

    
    

if __name__ == "__main__":
    weatherDetector = FindCurrentWeather()
    weatherDetector.detectRain()