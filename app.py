import requests

def fetchWeather():
        baseURL = "https://api.open-meteo.com/v1/forecast"
        latitude = "41.424010"
        longitude = "-81.949344"
        parameters = "latitude=" + latitude + "&longitude=" + longitude + "&current=temperature_2m"
        url = baseURL + "?" + parameters
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data["current"]["temperature_2m"]
            print(temp)
        else:
            print("Response not successful")

fetchWeather()
