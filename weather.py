#weather using api
"""import os
from xml.etree.ElementTree import PI
import requests #importing requests library to send http requests to the api
from dotenv import load_dotenv #importing load_dotenv to load environment variables from .env file
load_dotenv() #load environment variables from .env file
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("API_KEY") #get api key from environment variable
city = input("Enter city name: ")
complete_url = f"{base_url}appid={api_key}&q={city}" #appid is api key

try:
    response = requests.get(complete_url) #send request to api
    data = response.json() #get data in json format
    print(data) #print data to check if it is correct
except:
    print("Error fetching weather data")

if str(data["cod"]) != "404": #if city is found 404 is error code it should be equal to 404 to continue the process
    #If there is no error, continue the program
    main = data["main"] #get main dictionary
    weather = data["weather"][0] #get weather dictionary
    wind = data["wind"]["speed"] #get wind speed
    temperature = main["temp"] - 273.15 #get temperature in Celsius
    pressure = main["pressure"] #get pressure
    humidity = main["humidity"] #get humidity
    weather_description = weather["description"] #get weather description



    #print weather details
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Pressure: {pressure}hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")
    print(f"Weather Description: {weather_description}") 
else:
    print("City Not Found")#If city is not found, print error message """


import os
import requests
from dotenv import load_dotenv

load_dotenv()
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("API_KEY")
city = input("Enter city name: ")
complete_url = f"{base_url}appid={api_key}&q={city}"

try:
    response = requests.get(complete_url)
    data = response.json()
except Exception as e:
    print(f"Error fetching weather data: {e}")
    data = None

# Check if data was fetched AND if city was found
if data and str(data.get("cod")) != "404":
    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]["speed"]
    temperature = main["temp"] - 273.15
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather_description = weather["description"]

    print(f"Temperature: {temperature:.2f}°C")
    print(f"Pressure: {pressure}hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")
    print(f"Weather Description: {weather_description}") 
else:
    print("City Not Found")