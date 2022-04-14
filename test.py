import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Talin"
API_KEY = "82436636ffc425805b35ac7948ac986d"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"

response = requests.get(URL)

if response.status_code == 200:

   data = response.json()

   main = data['main']

   temperature = main['temp']

   report = data['weather']

   print("temperature:", temperature)

else:

   print("Error in the HTTP request")
