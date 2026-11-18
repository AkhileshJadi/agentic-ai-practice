import requests

url = 'https://jsonplaceholder.typicode.com/todos/999999'

try:

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    print(data["title"])

except requests.exceptions.Timeout:

    print("API requests time out")

except requests.exceptions.HTTPError as error:

    print("HTTP Error : ", error)

except requests.exceptions.RequestException as error:

    print("something went wrong", error)
