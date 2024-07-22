import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        weather_info = (
            f"Temperature: {temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Weather description: {weather_description.capitalize()}"
        )
        
        return weather_info
    else:
        return "City Not Found"

if __name__ == "__main__":
    api_key = 'b67dc76772573645e2b4f83f2b84db0b'
    city = input("Enter city name: ")
    
    weather_info = get_weather(api_key, city)
    print(weather_info)
