class Bird:
    def speak(self):
        return "aa"
class Dog:
    def speak(self):
        return "Woof!"
animals=[Bird(), Dog(),]
for animal in animals:
    print(animal.speak())