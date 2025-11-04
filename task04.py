import json
name=input("Ismingiz:")
age=input("Yoshingiz")
try:
    with open("data.json","r") as f:
        users=json.load(f)
except FileNotFoundError:
    users=[]
except json.JSONDecodeError:
    users=[]
new_user={"name": name, "age": int(age)}
users.append(new_user)
with open("data.json", "w") as f:
    json.dump(users, f, indent=4)