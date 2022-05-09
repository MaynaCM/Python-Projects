# program that collects user data from a specific location and returns the time details from that given location, using the Open Weather API #

# Here I've imported the requests and pretty print libraries, but first I've installed them using "pip install" in the termina l#
import requests 
from pprint import pprint 

# In this line you can see my API key, which is fundamental for the code to work correctly #
API_Key = '0d69a8e8bc38936fd75c73827541fba6'

# This is the user input. When is displayed, the user can type what city they want to check the weather infos #
city = input("Enter a city")

# Here I've used the API link, and then, using the "+" I'm concatenating the link with my API key and the city input#
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

# Then the response given by the url is stored in the "weather data" variable #
weather_data = requests.get(base_url).json()

# In this line I've just pretty printed the response stored in weather data! #
pprint(weather_data)
