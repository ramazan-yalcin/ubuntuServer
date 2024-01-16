import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q=Malatya&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    celsius = (temp - 32)/1.8

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {celsius}ºC")


