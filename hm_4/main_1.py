from __future__ import annotations

# Task 1
class Book:

    title: str
    author: str
    year: int

    def __init__(self, title: str, author: str, year: int):

        if year < 0: raise ValueError("Год выпуска не может быть отрицательным.")

        self.__title = title
        self.__author = author
        self.__year = year
        self.__bookmark = None

    def getInfo(self):
        return f"{self.__title}, {self.__author}, {self.__year}"

    def bookmarkPage(self, page: int) -> None:
        if page < 0: print("Закладка не установлена.")
        else:
            self.__bookmark = page
            print("Закладка установлена.")

    def updateTitle(self, new_title: str) -> None:
        self.__title = new_title
        print("Название изменено.")


class Library:

    name: str
    address: str
    books: list[Book]

    def __init__(self, name: str, address: str, books: list[Book]):
        self.__name = name
        self.__address = address
        self.__books = books

    def addBook(self, book: Book) -> None:
        if book not in self.__books:
            self.__books.append(book)
        else:
            print("Книга уже есть в библиотеке.")

    def removeBook(self, book: Book) -> None:
        if book in self.__books:
            self.__books.remove(book)
        else:
            print("Такой книги нет в библиотеке.")

    def listBooks(self) -> list[str]:
        result = [book.getInfo() for book in self.__books]
        return result


print("--------------------------------------------------------------------------")
lib = Library("Центральная библиотека", "ул. Ленина, 10", [])
b1 = Book("Война и мир", "Л. Толстой", 1869)
b2 = Book("Мастер и Маргарита", "М. Булгаков", 1967)
lib.addBook(b1)
lib.addBook(b2)
print(b1.getInfo())
print(lib.listBooks())


# Task 2
class Student:

    def __init__(self, name: str, id: int, grades: list[int]):
        self.__name = name
        self.__id = id
        self.__grades = grades

    def get_id(self):
        return self.__id

    def get_profile(self) -> str:
        return f"Студент: {self.__name}, ID: {self.__id}"

    def assign_grade(self, grade: int) -> None:
        self.__grades.append(grade)


class Faculty:

    def __init__(self, name: str, students: list[Student]):
        self.__name = name
        self.__students = students

    def get_name(self):
        return self.__name

    def enroll(self, student: Student) -> None:
        if student not in self.__students:
            self.__students.append(student)
        else:
            print("Студент уже на факультете.")

    def graduate(self, student: Student) -> None:
        if student in self.__students:
            self.__students.remove(student)
        else:
            print("Студента нет на факультете.")

    def list_students(self):
        result = [stud.get_profile() for stud in self.__students]
        return result

    def find_student(self, id: str) -> Student | None:
        for stud in self.__students:
            if stud.get_id() == id:
                return stud


class University:

    def __init__(self, name: str, faculties: list[Faculty]):
        self.__name = name
        self.__faculties = faculties

    def add_faculty(self, f: Faculty) -> None:
        if f not in self.__faculties:
            self.__faculties.append(f)
        else:
            print("Факультет уже есть в списке университета.")

    def remove_faculty(self, f: Faculty) -> None:
        if f in self.__faculties:
            self.__faculties.remove(f)
        else:
            print("Такого фалькультета нет в списке университета.")

    def list_faculties(self):
        return [fac.get_name() for fac in self.__faculties]

    def find_faculty(self, name: str) -> Faculty | None:
        for _ in self.__faculties:
            if _.get_name() == name:
                return _

print("--------------------------------------------------------------------------")
uni = University("МГУ", [])
math = Faculty("Математический факультет", [])
ivan = Student("Иван Иванов", 12345, [])
uni.add_faculty(math)
math.enroll(ivan)
print(uni.list_faculties()) # ['Математический факультет']
print(math.list_students()) # ['Иван Иванов (12345)']
profile = ivan.get_profile()
print(profile) # Студент: Иван Иванов, ID: 12345


# Task 3
class Engine:

    def __init__(self, power: int, type: str):

        if power < 0: raise ValueError("Энергия двигателя не может быть отрицательной.")
        if type.lower() not in ["бензиновый", "дизельный", "водородный"]: raise ValueError("Двигателя такого типа не может быть.")

        self.__power = power
        self.__type = type
        self.__is_working = "остановлен"

    def ignite(self) -> None:
        if self.__is_working == "остановлен":
            self.__is_working = "работает"
            print("Двигатель был запущен.")
        else:
            print("Двигатель уже запущен.")

    def shutdown(self) -> None:
        if self.__is_working == "работает":
            self.__is_working = "остановлен"
            print("Двигатель был остановлен.")
        else:
            print("Двигатель и так не запущен.")

    def service(self) -> None:
        if self.__is_working != "на обслуживании":
            self.__is_working = "на обслуживании"
            print("Двигатель переведён на обслуживание.")
        else:
            print("Двигатель и так нa обслуживании.")

    def get_power(self) -> int:
        return self.__power

    def get_type(self) -> str:
        return self.__type

    def status(self) -> str:
        return self.__is_working


class Wheel:

    def __init__(self, size: int, type: str):

        if size < 1: raise ValueError("Диаметр кодеса не может быть < 1 дюйма.")
        if type.lower() not in ["летняя", "зимняя", "всесезонная"]: raise ValueError("Такого типа резины не может стоять на колесе.")

        self.__size = size
        self.__type = type
        self.__pressure = 10

    def rotate(self) -> None:
        print("Колесо вращается...")

    def inflate(self, pressure: float) -> None:
        if 91 > pressure > 9:
            self.__pressure = pressure
        else:
            print("Заданное давление БР недопустимо.")

    def deflate(self) -> None:
        self.__pressure = 10

    def get_size(self) -> int:
        return self.__size

    def get_type(self) -> str:
        return self.__type

    def get_pressure(self):
        return self.__pressure


class Car:

    def __init__(self, brand: str, model: str, engine: Engine, wheels: list[Wheel]):

        if len(wheels) != 4: raise ValueError("Количество колёс != 4.")
        if len(set(wheels)) != len(wheels): raise ValueError("Одно колесо не может стоять на нескольких местах сразу...")

        self.__brand = brand
        self.__model = model
        self.__engine = engine
        self.__wheels = wheels

    def start(self) -> None:
        if self.__engine.status() != "работает":
            if all(filter(lambda a: a.get_pressure() > 10, self.__wheels)):
                self.__engine.ignite()
            else:
                print("Машина не была запущена, проверьте давление колёс.")
        else:
            print("Машина уже запущена...")

    def stop(self) -> None:
        if self.__engine.status() != "остановлен":
            self.__engine.shutdown()
            print("Машина была остановлена.")
        else:
            print("Машина уже остановлена.")

    def get_specs(self) -> str:
        return f"{self.__brand} - {self.__model}, двигатель: {self.__engine.get_type()} - {self.__engine.get_power()} кВт."

    def replace_wheel(self, idx: int, new: Wheel) -> None:
        if 0 <= idx <= 3:
            if new not in self.__wheels:
                self.__wheels[idx] = new
            else:
                print("Нельзя заменить колесо на уже прикреплённое к машине другое колесо.")
        else:
            print("Введён недопустимый номер места для колеса.")

print("--------------------------------------------------------------------------")
engine = Engine(power=150, type="бензиновый")
w1 = Wheel(size=16, type="всесезонная")
w2 = Wheel(size=16, type="всесезонная")
w3 = Wheel(size=16, type="всесезонная")
w4 = Wheel(size=16, type="всесезонная")
car = Car(brand="Toyota", model="Camry", engine=engine, wheels=[w1, w2, w3, w4])
car.start()
new_wheel = Wheel(size=16, type="зимняя")
car.replace_wheel(2, new_wheel)
print(car.get_specs())
car.stop()


# Task 4
import datetime

class OrderItem:

    def __init__(self, item_name: str, count=1):

        if not isinstance(count, int): raise TypeError("Количество предметов может быть только целым.")
        if count < 1: raise ValueError("Количество предметов не может быть < 0.")

        self.__item_name = item_name
        self.__count = count

    def __str__(self):
        return f"{self.__item_name} - {self.__count} штук(а/и)."

    def __add__(self, other_item):
        if self.__item_name == other_item.get_item_name:
            return OrderItem(self.__item_name, self.__count + other_item.get_count())

    def get_item_name(self):
        return self.__item_name

    def get_count(self):
        return self.__count


class Client:

    def __init__(self, client_id: str, name: str, email: str, orders: list[Order]):

        if len(orders) != len(set(orders)): raise ValueError("Один и тот же заказ не может быть в списке > 1 раза.")

        self.__client_id = client_id
        self.__name = name
        self.__email = email
        self.__orders = orders

    def place_order(self, order: Order) -> None:
        if order not in self.__orders:
            self.__orders.append(order)
        else:
            print("Добавленный заказ уже в заказах пользователя.")

    def get_client_id(self):
        return self.__client_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_orders(self) -> list[Order]:
        return [order for order in self.__orders]


class Order:

    def __init__(self, order_id: str, date: datetime.date, client: Client, items: list[OrderItem]):

        if len(set(items)) != len(items): raise ValueError("Один и тот же предмет(объект) не может быть заказан > 1 раза.")

        self.__order_id = order_id
        self.__date = date
        self.__client = client
        self.__items = items

    def add_item(self, order_item: OrderItem) -> None:
        if order_item.get_item_name() in self.__items:
            for i in range(len(self.__items)):
                if self.__items[i].get_item_name() == order_item.get_item_name():
                    self.__items[i] = self.__items[i] + order_item
                    break
        else:
            self.__items.append(order_item)

    def get_order_id(self):
        return self.__order_id

    def get_date(self):
        return self.__date

    def get_clients(self):
        return self.__client

    def get_items(self):
        return [item for item in self.__items]

    def get_summary(self) -> str:
        return f"Заказ {self.__order_id} от {self.__date} для {self.__client.get_name()}(id: {self.__client.get_client_id()}): {[item.__str__() for item in self.__items]}"


print("--------------------------------------------------------------------------")
client = Client("C001", "Анна Петрова", "anna@example.com", [])
order = Order("O1001", datetime.date.today(), client, [])
client.place_order(order)
item = OrderItem("Книга", 2)
order.add_item(item)
print(client.get_orders())
print(order.get_summary()) # Заказ O1001 от 2025-06-24 для Анна Петрова: Книга (в количестве: 2)