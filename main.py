import requests

url = "https://api.hh.ru/vacancies/"
params = {"text": "Программист"}
response = requests.get(url, params=params)
response.raise_for_status()
print(response.json())
