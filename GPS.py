import requests


class FindCurrentLocation:
    def locationCordinates(self):
        try:
            response = requests.get('https://ipinfo.io')
            response_json = response.json()
            location = response_json['loc'].split(',')
            latitude = float(location[0])
            longitute = float(location[1])
            city = response_json.get('city', 'Unknown')
            state = response_json.get('region', 'Unknown')
            response_json = {'city': city, 'state': state, 'latitude': latitude, 'longitute': longitute}
            return response_json

        except:
            print("Internet not avialable")
            exit()

    
if __name__ == "__main__":
    location = FindCurrentLocation()
    current_location = location.locationCordinates()
    print(current_location)