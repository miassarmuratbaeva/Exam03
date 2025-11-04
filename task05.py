import json
try:
    with open("data.json", "r") as f:
       users=json.load(f)
    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}")
except FileNotFoundError:
    print("Fayl topilmadi")