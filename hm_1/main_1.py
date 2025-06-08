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



# Task 3

class PassengerPlane:

    made_by: str
    model: str
    passenger_capacity: int
    in_fly: bool
    height: int
    speed: int

    def __init__(self, made_by: str, model: str, passenger_capacity: int, in_fly: bool, height: int, speed: int):
        self.made_by = made_by
        self.model = model
        self.passenger_capacity = passenger_capacity
        self.in_fly = in_fly
        self.height = height
        self.speed = speed


    def __str__(self):
        return (f"Производитель: {self.made_by};"
                f"\nМодель: {self.model};"
                f"\nВместимость пассажиров: {self.passenger_capacity};"
                f"\nВысота: {self.height};"
                f"\nСкорость: {self.speed}.")


    def set_fly_status(self, new_status: bool):
        if new_status == self.in_fly:
            result = f"Статус полёта не был изменён."
        else:
            self.in_fly = new_status
            result = f"Статус полёта изменён на {new_status}."

        return result


    def set_height(self, new_height: int):
        if (new_height < 0) or (new_height > 15000):
            return f"Невозможно перевести самолёт на такую высоту (0 <= высота <= 15000)."

        if new_height == 0:
            self.height = new_height
            self.in_fly = False
            return f"Самолет приземлился!"

        if new_height == self.height:
            return f"Высота не была изменена."

        if (self.speed < 230) and (self.height == 0) and (new_height > 0):
            return f"Скорость слишком мала для взлёта (мин. 230)."

        if (self.speed >= 230) and (self.height == 0) and (new_height > 0):
            self.height = new_height
            self.in_fly = True
            return f"Самолет взлетел!"

        self.height = new_height
        return f"Установлена новая высота."


    def set_speed(self, new_speed: int):
        if (new_speed < 0 or new_speed > 300) and self.in_fly is False:
            return f"Невозможно перевести самолёт на такую скорость на земле (0 <= скорость <= 300)."

        if (new_speed <= 300 or new_speed > 800) and self.in_fly is True:
            return f"Невозможно перевести самолёт на такую скорость в полёте (300 <= скорость <= 800)."

        self.speed = new_speed
        return f"Установлена новая скорость."



# Task 4

class Track:

    name: str
    executor: str
    duration: int or float
    genre: str

    def __init__(self, name: str, executor: str, duration: int or float):
        self.name = name
        self.executor = executor
        self.duration = duration



class MusicAlbum:

    name: str
    executor: str
    genre: str
    track_list: list[Track]

    def __init__(self, name: str, executor: str, genre: str, track_list: list[Track]):
        self.name = name
        self.executor = executor
        self.genre = genre
        self.track_list = track_list


    def __str__(self):
        return (f"Название: {self.name};\n"
                f"Исполнитель: {self.executor};\n"
                f"Жанр: {self.genre};\n"
                f"Список треков: {self.track_list}.")       # Вопрос


    def add_track(self, track: Track):
        if track not in self.track_list:
            self.track_list.append(track)
            return f"Трек с названием '{track.name}' был удалён из альбома."
        else:
            return f"Трек с названием '{track.name}' уже есть в альбоме {self.name}."


    def delete_track(self, track: Track):
        if track in self.track_list:
            self.track_list.remove(track)
        else:
            return f"Трека с таким названием нет в альбоме '{self.name}'."


    def play_track(self, track: Track):
        if track in self.track_list:
            return f"Воспроизведение трека '{track.name}'."
        else:
            return f"Трека с таким названием нет в альбоме '{self.name}'."