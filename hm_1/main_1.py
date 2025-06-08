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



# Task 2

class Book:

    name: str
    author: str
    page_count: int

    def __init__(self, name: str, author: str, page_count: int):
        self.name = name
        self.author = author
        self.page_count = page_count


    def __str__(self):
        return f"Название книги: {self.name};\nАвтор: {self.author};\nКоличество страниц: {self.page_count}."


    def open_page(self, page_number: int):
        if (page_number > self.page_count) or (page_number < 1):
            result = f"Такой страницы не существует."
        else:
            result = f"Страница №{page_number} открылась."

        return result