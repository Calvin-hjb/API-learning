import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes": 11658, "name": "Tim", "views": 10000},
        {"likes": 2568, "name": "Bella", "views": 4658},
        {"likes": 79, "name": "Jess", "views": 10000000000}
        ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0", json={})
print(response) 

input()

response = requests.get(BASE + "video/2", json={})
print(response.json()) 