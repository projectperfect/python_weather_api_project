import requests

api_key = ""

def get_weather(city, units="metric", api_key=""):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open("data.txt", "a") as file:
    for item in content["list"]:
      file.write(f'{item["dt_txt"]}, {item["main"]["temp"]}, {item["weather"][0]["description"]}\n')

print(get_weather(city="Washington"))