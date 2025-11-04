name=input("Ismingiz:")
age=input("Yoshingiz:")
with open("data.txt", "a") as f:
    f.write(f"{name}-{age}\n")
print("Malumot faylga yozildi.")