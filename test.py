import requests

BASE = " http://127.0.0.1:5000/"
# data = [
#     {"likes": 10, "name": "Jack", "views": 1000},
#     {"likes": 1000, "name": "Frank", "views": 80000},
#     {"likes": 80, "name": "Fin", "views": 100}
# ]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()
# response = requests.delete(BASE + "video/0")
# print(response)

# input()
# response = requests.get(BASE + "video/2")
# print(response.json())

# input()
response = requests.patch(BASE + "video/2", {"likes": 1001, "views": 100})
print(response.json())
