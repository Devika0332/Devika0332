Import requests
#import os
From datetime import datetime

Api_key = ‘87d845b0b6cf29baa1a73cc34b067a95’
Location = input(“Enter the city name: “)

Complete_api_link = https://api.openweathermap.org/data/2.5/weather?q=+location+”&appid=”+api_key
Api_link = requests.get(complete_api_link)
Api_data = api_link.json()

#create variables to store and display data
Temp_city = ((api_data[‘main’][‘temp’]) – 273.15)
Weather_desc = api_data[‘weather’][0][‘description’]
Hmdt = api_data[‘main’][‘humidity’]
Wind_spd = api_data[‘wind’][‘speed’]
Date_time = datetime.now().strftime(“%d %b %Y | %I:%M:%S %p”)

Print (“-------------------------------------------------------------“)
Print (“Weather Stats for – {}  || {}”.format(location.upper(), date_time))
Print (“-------------------------------------------------------------“)

Print (“Current temperature is: {:.2f} deg C”.format(temp_city))
Print (“Current weather desc  :”,weather_desc)
Print (“Current Humidity      :”,hmdt, ‘%’)
Print (“Current wind speed    :”,wind_spd ,’kmph’)
