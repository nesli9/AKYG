import requests

URL = "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
result = requests.get(URL)

data = result.json()

print(data)
