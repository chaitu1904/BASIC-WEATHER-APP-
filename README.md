# BASIC-WEATHER-APP-
Import requests:

The requests library is used to make HTTP requests to the OpenWeatherMap API.
Define the get_weather function:

Constructs the URL to fetch weather data for the specified city.
Sends a GET request to the API and parses the JSON response.
Extracts relevant weather information such as temperature, pressure, humidity, description, and wind speed.
Returns a formatted string containing the weather report.
Define the main function:

Prompts the user to enter a city name.
Calls the get_weather function with the city name and API key.
Prints the weather report.
Execution block:

Ensures the main function runs when the script is executed.
This basic app will prompt the user to enter a city name and then display the current weather information for that city using the OpenWeatherMap API.






