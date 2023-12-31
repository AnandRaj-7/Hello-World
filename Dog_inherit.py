class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return f"{self.name} says {sound}"
rocky = GoldenRetriever("Rocky", 10)
print(rocky.speak())