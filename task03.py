try:
    with open("data.txt", "r") as f:
        lines=len(f.readlines())
        print(f"data.txt faylida {lines}ta foydalanuvchi mavjud")
except FileNotFoundError:
    print("Fayl topilmadi")