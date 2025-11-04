class Animal:
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound
    def make_sound(self):
        return f"{self.name} says {self.sound}!"
animal1 = Animal("Dog", "Woof")
animal2 = Animal("Cat", "Meow")
print(animal1.make_sound())
print(animal2.make_sound())