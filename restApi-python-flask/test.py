import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"name": "In the name of the father", "likes": 324,  "views": 894000}, {"name": "Saving Private Ryan", "likes": 256, "views": 423500}, {"name": "Garfield", "likes": 8,  "views": 121}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()

# response = requests.get(BASE + "video/6")
# print(response.json())

response = requests.patch(BASE + "video/2", {"name": "starwars", "views":3})
print(response.json())