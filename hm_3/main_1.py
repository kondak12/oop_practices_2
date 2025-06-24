class BankAccount:

    owner: str
    balance: float

    def __init__(self, owner: str, balance: float):
        self.__owner = owner
        self.__balance = balance

    def get_owner(self) -> str:
        return self.__owner

    def get_balance(self) -> float:
        return self.__balance

    def set_owner(self, owner: str):
        if not isinstance(owner, str): TypeError("Введена переменная другого типа данных (не str).")
        self.__owner = owner

    def set_balance(self, amount: float):
        if not isinstance(amount, (int, float)): TypeError("Введена переменная другого типа данных (не int или float).")
        if amount < 0: ValueError("Введённое значение не должно быть отрицательным.")
        self.__balance = amount


print("\n--------------------------------------------BankAccount")
acct = BankAccount("Иван Иванов", 1000.0)
print(acct.get_owner()) # "Иван Иванов"
print(acct.get_balance()) # 1000.0
acct.set_owner("Пётр Петров")
acct.set_balance(2500.75)
print(acct.get_owner()) # "Пётр Петров"
print(acct.get_balance()) # 2500.75



class Rectangle:

    width: float
    height: float

    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def area(self) -> float:
        return self.__height*2 + self.__width*2

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def set_width(self, w: float):
        if not isinstance(w, (int, float)): TypeError("Введена переменная другого типа данных (не int или float).")
        if w < 1: ValueError("Введённое значение не должно быть больше нуля.")
        self.__width = w

    def set_height(self, h: float):
        if not isinstance(h, (int, float)): TypeError("Введена переменная другого типа данных (не int или float).")
        if h < 1: ValueError("Введённое значение не должно быть больше нуля.")
        self.__height = h


print("\n--------------------------------------------Rectangle")
rect = Rectangle(3.5, 4.2)
w = rect.get_width() # 3.5
h = rect.get_height() # 4.2
print(f"Ширина={w}, высота={h}")
rect.set_width(5)
rect.set_height(2.8)
print("Площадь:", rect.area()) # 14.0



class Student:

    name: str
    grades: list[int or float]

    def __init__(self, name: str, grades: list[int or float]):
        self.__name = name
        self.__grades = grades

    def average(self) -> float:
        return sum(self.__grades) / len(self.__grades)

    def get_name(self) -> str:
        return self.__name

    def get_grades(self) -> list:
        return self.__grades

    def set_name(self, name: str):
        if not isinstance(name, str): TypeError("Введена переменная другого типа данных (не str).")
        self.__name = name

    def set_grades(self, grades: list):
        if not isinstance(grades, list): TypeError("Введена переменная другого типа данных (не str).")
        if False in map(lambda elem: not isinstance(elem, (int or float)), grades): TypeError("Один или несколько элементов списка не является переменной с типом данных int или float.")
        self.__grades = grades


print("\n--------------------------------------------Student")
stu = Student("Мария", [4, 5, 3, 5])
print(stu.get_name()) # "Мария"
print(stu.get_grades()) # [4, 5, 3, 5]
stu.set_grades([5, 5, 4, 4, 5])
print("Средний балл:", stu.average()) # 4.6



class TemperatureLog:

    city: str
    temperatures: list[int or float]

    def __init__(self, city: str, temperatures: list[int or float]):

        if len(temperatures) > 7 or len(temperatures) < 7: ValueError("Количество температур за неделю не равно 7.")

        self.__city = city
        self.__temperatures = temperatures

    def average_temp(self) -> float:
        return sum(self.__temperatures) / len(self.__temperatures)

    def max_temp(self) -> float:
        return max(self.__temperatures)

    def min_temp(self) -> float:
        return min(self.__temperatures)

    def get_city(self) -> str:
        return self.__city

    def get_temperatures(self) -> list:
        return self.__temperatures

    def set_city(self, city: str):
        if not isinstance(city, str): TypeError("Введена переменная другого типа данных (не str).")
        self.__city = city

    def set_temperatures(self, temps: list):
        if len(temps) > 7 or len(temps) < 7: ValueError("Количество температур за неделю не равно 7.")
        if False in map(lambda elem: not isinstance(elem, (int or float)), temps): TypeError("Один или несколько элементов списка не является переменной с типом данных int или float.")
        self.__temperatures = temps


print("\n--------------------------------------------TemperatureLog")
log = TemperatureLog("Москва", [21.5, 22.0, 19.8, 20.1, 23.3, 18.9, 21.0])
print("Город:", log.get_city())
log.set_temperatures([20, 21, 19, 18, 22, 23, 20])
print("Средняя:", log.average_temp()) # 20.428...
print("Максимальная:", log.max_temp()) # 23
print("Минимальная:", log.min_temp()) # 18


class EmployeePayroll:

    name: str
    salary: int or float
    tax_rate: int or float

    def __init__(self, name: str, salary: int or float, tax_rate: int or float):
        self.__name = name
        self.__salary = salary
        self.__tax_rate = tax_rate

    def net_salary(self) -> int or float:
        return self.__salary * (1 - self.__tax_rate)

    def annual_net(self) -> int or float:
        return 12 * self.net_salary()

    def get_name(self) -> str:
        return self.__name

    def get_salary(self) -> int or float:
        return self.__salary

    def get_tax_rate(self) -> int or float:
        return self.__tax_rate

    def set_name(self, name: str):
        if not isinstance(name, str): TypeError("Введена переменная другого типа данных (не str).")
        self.__name = name

    def set_salary(self, sal: int or float):
        if not sal >= 0: ValueError("Новое значение salary не должно быть отрицательным.")
        self.__salary = sal

    def set_tax_rate(self, rate: int or float):
        if not 0 <= rate <= 1: ValueError("Новое значение rate не должно быть в диапазоне [0 : 1].")
        self.__tax_rate = rate


print("\n--------------------------------------------EmployeePayroll")
e1 = EmployeePayroll("Анна", 50000.0, 0.13)
e2 = EmployeePayroll("Борис", 75000.0, 0.20)
print(e1.get_name(), "net:", e1.net_salary(), "annual net:", e1.annual_net())
print(e2.get_name(), "net:", e2.net_salary(), "annual net:", e2.annual_net())
e1.set_salary(52000)
e1.set_tax_rate(0.15)
print("После изменения:", e1.get_name(), "net:", e1.net_salary())