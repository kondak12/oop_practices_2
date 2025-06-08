# Task 1

class Animal:

    name: str
    type: str
    age: int

    def __init__(self, name: str, type: str, age: int):
        self.name = name
        self.type = type
        self.age = age


    def __str__(self):
        return f"Имя: {self.name};\nВид: {self.type};\nВозраст: {self.age}."


    def get_sound(self, sound: str):
        return f"{self.type} издаёт звук: '{sound}'."


