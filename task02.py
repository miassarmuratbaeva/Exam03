try:
    with open("data.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Fayl topilmadi")