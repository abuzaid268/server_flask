import requests

fur_name = input("enter fur\n")
url = 'http://localhost:3000/buy/{}'.format(fur_name)
res = requests.get(url=url)
print(res.json())