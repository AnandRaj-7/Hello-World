##### 10.4 Challenge: Model A Farm #####
class Animal:
    def __init__(self, type, sound, age):
        self.type = type
        self.sound = sound
        self.age = age
    def __str__(self):
        return f"This is a {self.type} of age {self.age}"
    def purpose(self):
        print("This is an animal raised in farm")
class Cow(Animal):
    def __init__(self, type, sound, age, breed):
        super().__init__(type, sound, age)
        self.breed = breed
    def __str__(self):
        return f"{super().__str__()}\nThis is a Cow of breed {self.breed} and sounds {self.sound}"
    def purpose(self):
        super().purpose()
        print("This is a cow raised for milk and milk products !!")
class Pig(Animal):
    def __init__(self, type, sound, age, breed):
        super().__init__(type, sound, age)
        self.breed = breed
    def __str__(self):
        return f"{super().__str__()}\nThis is a Pig of breed {self.breed} and sounds {self.sound}"
        def purpose(self):
            super().purpose()
            print("This is a pig raised for meat and leather !!")
class Horse(Animal):
    def __init__(self, type, sound, age, breed):
        super().__init__(type, sound, age)
        self.breed = breed
    def __str__(self):
        return f"{super().__str__()}\nThis is a Horse of breed {self.breed} and sounds {self.sound}"
    def purpose(self):
        super().purpose()
        print("This is a horse used for gaurding by cow boys. It is a beast of burden cattle")
farm_animal = Animal("Cattle", "Moo", 10)
print(type(farm_animal))
print(farm_animal)
farm_animal.purpose()
cow1 = Cow("Cattle", "Moo", 10, "Holstein Friesian")
print(type(cow1))
print(cow1)
cow1.purpose()
cow2 = Cow("Cattle", "Moo", 11, "Jersey")
print(type(cow2))
print(cow2)
cow2.purpose()
pig1 = Pig("Cattle", "Oink", 10, "Chester White")
print(type(pig1))
print(pig1)
pig1.purpose()
horse1 = Horse("Beast of burden", "Neigh", 8, "Thoroughbred")
print(type(horse1))
print(horse1)
horse1.purpose()