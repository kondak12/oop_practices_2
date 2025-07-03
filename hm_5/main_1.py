import abc


# Task 1
class Vehicle(abc.ABC):

    name: str
    max_speed: float

    def __init__(self, name: str, max_speed: float):

        if not isinstance(name, str): raise TypeError
        if not isinstance(max_speed, (int, float)): raise TypeError
        if max_speed < 0: raise ValueError

        self._name = name
        self._max_speed = max_speed

    @abc.abstractmethod
    def move(self) -> str:
        pass

    @abc.abstractmethod
    def fuel_consumption(self, distance_km: float) -> float:
        pass

    def get_name(self):
        return self._name

    def get_max_speed(self):
        return self._max_speed


class Car(Vehicle):

    fuel_efficiency_100km: float

    def __init__(self, name: str, max_speed: float, fuel_efficiency_100km: float):

        if not isinstance(fuel_efficiency_100km, (int, float)): raise TypeError

        super().__init__(name, max_speed)
        self.__fuel_efficiency_100km = fuel_efficiency_100km

    def move(self) -> str:
        return f"{self._name} (машина) едет по дороге"

    def fuel_consumption(self, distance: float) -> float:
        if not isinstance(distance, (int, float)): raise ValueError
        return distance * self.__fuel_efficiency_100km / 100

    def get_fuel_efficiency_100km(self):
        return self.__fuel_efficiency_100km


class Bicycle(Vehicle):

    def __init__(self, name: str, max_speed: int):
        super().__init__(name, max_speed)

    def move(self) -> str:
        return f"{self._name} (велосипед) едет по дороге"

    def fuel_consumption(self, distance_km: float) -> float:
        return 0.0


# Пример использования:
print("-------------------------------------------------")
vehicles = [
Car(name="Toyota Camry", max_speed=210, fuel_efficiency_100km=7.5),
Bicycle(name="Stels Navigator", max_speed=30)
]
for v in vehicles:
    print(v.move())
    print(f"Расход на 50 км: {v.fuel_consumption(50):.2f} л")

# Task 2
class Animal(abc.ABC):

    name: str
    age: int

    def __init__(self, name: str, age: int):

        if not isinstance(name, str): raise TypeError
        if not isinstance(age, int): raise TypeError
        if not 0 <= age <= 300: raise ValueError

        self._name = name
        self._age = age

    @abc.abstractmethod
    def speak(self) -> str:
        pass

    @abc.abstractmethod
    def move(self) -> str:
        pass

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Dog(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def speak(self) -> str:
        return f"{self._name} лает!"

    def move(self) -> str:
        return f"{self._name} бежит"


class Bird(Animal):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def speak(self) -> str:
        return f"{self._name} чирикает!"

    def move(self) -> str:
        return f"{self._name} летит"


# Пример использования:
print("-------------------------------------------------")
pets = [
Dog(name="Барбос", age=4),
Bird(name="Кеша", age=1)
]
for p in pets:
    print(f"{p.get_name()}, {p.get_age()} года(лет): {p.speak()}, {p.move()}.")


# Task 3
class Employee(abc.ABC):

    name: str
    base_salary: float

    def __init__(self, name: str, base_salary: float):

        if not isinstance(name, str): raise TypeError
        if not isinstance(base_salary, (int, float)): raise TypeError
        if base_salary <= 0: raise ValueError

        self._name = name
        self._base_salary = base_salary

    @abc.abstractmethod
    def calculate_salary(self) -> float:
        return self._base_salary

    def get_name(self):
        return self._name


class Developer(Employee):

    bonus: float

    def __init__(self, name: str, base_salary: float, bonus: float):

        if not isinstance(bonus, (int, float)): raise TypeError
        if bonus < 0: raise ValueError

        super().__init__(name, base_salary)
        self.__bonus = bonus

    def calculate_salary(self) -> float:
        return self._base_salary + self.__bonus

    def get_bonus(self):
        return self.__bonus


class Manager(Employee):

    team_size: int
    per_person_bonus: float

    def __init__(self, name: str, base_salary: float, team_size: int, per_person_bonus: float):

        if not isinstance(team_size, int): raise TypeError
        if not isinstance(per_person_bonus, (int, float)): raise TypeError
        if team_size < 1: raise ValueError
        if per_person_bonus < 0: raise ValueError

        super().__init__(name, base_salary)
        self.__team_size = team_size
        self.__per_person_bonus = per_person_bonus

    def calculate_salary(self):
        return self._base_salary + self.__team_size * self.__per_person_bonus

    def get_team_size(self):
        return self.__team_size

    def get_per_person_bonus(self):
        return self.__per_person_bonus


# Пример использования:
print("-------------------------------------------------")
staff = [
Developer(name="Алиса", base_salary=100_000, bonus=20_000),
Manager(name="Борис", base_salary=120_000, team_size=5, per_person_bonus=5_000)
]
for emp in staff:
    print(f"{emp.get_name()}: итоговый оклад = {emp.calculate_salary():,.0f} руб.")