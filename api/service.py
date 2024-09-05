from datetime import datetime
from store import SoilStore
from schemas import SoilSample, Farmer
from geopy.geocoders import Nominatim
from config import settings

import requests
# import pywhatkit

API_URL = settings.weather_api_url
API_KEY = settings.weather_api_key

class SoilService:

    def __init__(self, store: SoilStore):
        self._store = store

    def add_farmer(self, request: Farmer):
        farmer_data = Farmer(
            created_at=datetime.now(),
            **request.model_dump()
        )
        return self._store.add_farmer(farmer=farmer_data)
        

    def add_sample(self, farmer_uname, area_name, city_name):
        
        farmer_id, farmer_phone = self._store.get_farmer(uname=farmer_uname)

        loc = Nominatim(user_agent="GetLoc")
        getLoc = loc.geocode(f"{area_name} {city_name}")

        latitude = getLoc.latitude
        longitude = getLoc.longitude
        address = getLoc.address

        url =  f"{API_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}"
        with requests.Session() as session:
            response = session.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                temperature = weather_data['main']['temp'] - 273.15 # Converted Into Celcius 
                humidity = weather_data['main']['humidity']
                weather_description = weather_data['weather'][0]['description']
                if temperature > 30:
                    respone = "Temperature in the surrounding is very high, Water the plant"
                    need_water = 1
                elif humidity < 30:
                    respone ="Humidity is very low, Water the plant"
                    need_water = 1
                elif 'rain' not in weather_description or 'thunderstorm' not in weather_description:
                    respone ="Rain is not going to happen now, Water the plant"
                    need_water = 1
                else:
                    respone = "You don't have to Water the plant now."
                    need_water = 0

        sample = SoilSample(
            farmer_id=farmer_id,
            address=address,
            latitude=latitude,
            longitude=longitude,
            need_water=need_water,
            created_at=datetime.now(),
        )
        self._store.add_sample(sample=sample)

        # pywhatkit.sendwhatmsg_instantly(farmer_phone, respone) #phone no must have +91 contry code

        return respone