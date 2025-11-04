import json
class User:
    def __init__(self, username, email, is_active=True):
        self.username=username
        self.email=email
        self.is_active=is_active
    def save(self):
        try:
            with open("users.json", "r") as f:
                users=json.load(f)
        except FileNotFoundError:
            users=[]
        user_data={
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active
        }
        users.append(user_data)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)
    def deactivate(self):
        self.is_active=False
user1=User("miiassarm", "miiassarm@gmail.com", True)
user2=User("sarvinoz04", "usmonovaa@gmail.com", False)
user1.save()
user2.save()
with open("users.json", "r") as f:
        all_users=json.load(f)
        print("Jami  foydalanuvchilar:")
        for u in all_users:
            if u["is_active"]:
                status="Active"
            else:
                status="Inactive"
            print(f"Username: {u['username']}, Email: {u['email']}, Status: {status}")