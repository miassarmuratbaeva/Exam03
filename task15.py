class AgeError(Exception):
    pass
age=int(input("Yoshingiz:"))
if age < 0:
    raise AgeError("Yosh notogri!")
else:
    print(f"Sizning yoshingiz: {age}")