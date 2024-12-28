import requests

def fetchWeather():
        baseURL = "https://api.open-meteo.com/v1/forecast"
        latitude = "34.434"
        longitude = "24.345"
        parameters = "latitude=" + latitude + "&longitude=" + longitude + "&current=temperature_2m,wind_speed_10m&hourly=temperature_2m"
        url = baseURL + "?" + parameters
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temp = data["current"]["temperature_2m"]
            tempF = (temp * 1.8) + 32
            hourlyTemp = data["hourly"]["temperature_2m"]
            print("Temperature: %.1f°C / %.1f°F" % (temp, tempF))
            maximumTemp = 0
            maxHour = 0
            minimumTemp = 100
            minHour = 0
            for i in range(0, len(hourlyTemp) - 1):
                if maximumTemp < hourlyTemp[i]:
                     maximumTemp = hourlyTemp[i]
                     maxHour = i
            for i in range(0, len(hourlyTemp) - 1):
                 if minimumTemp > hourlyTemp[i]:
                      minimumTemp = hourlyTemp[i]
                      minHour = i

            print("The highest temperature this week will be %.1f°C in %d hours." % (maximumTemp, maxHour))
            print("The lowest temperature this week will be %.1f°C in %d hours." % (minimumTemp, minHour)) 
                
        else:
            print("Response not successful")

fetchWeather()
