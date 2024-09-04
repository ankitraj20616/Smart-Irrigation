import requests
class  findCurrentWeather : 

    # Requesting to gather the IP Information from the Open source API 

    request_data = requests.get('https://ipinfo.io/')

    # Requested data is to stored in JSON Format for accessing of Data

    dataRead=request_data.json() 
    # print(dataRead)

    #From The data we have read we are taking out the City Location from the JSON format
    cityCurrentLocation = dataRead['city']
    print(f"THE CURRENT CITY LOCATION IS : {cityCurrentLocation}")
    
    # Giving the URL Current Location of the city In Open Source Weather Api
    url = 'https://wttr.in/{}'.format(cityCurrentLocation)

    # Gathering the current city location weather and printing the request data 
    request_url= requests.get(url)

    print(request_url.text)

