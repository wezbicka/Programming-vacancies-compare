import requests

url = "https://api.hh.ru/vacancies/"
payload = {
    "text": "Программист",
    "area": "1",
    "period": 30
    }
response = requests.get(url, params=payload)
response.raise_for_status()
print(response.json())
print(response.json()["found"])
print(response.url)
