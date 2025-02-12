import requests

question_data = []
parameters = {
    "amount":10,
    "type":"boolean"
}

url = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]