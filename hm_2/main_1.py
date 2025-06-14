# 1
from __future__ import annotations

class Point2D:

    x: int or float
    y: int or float

    def __init__(
            self,
            x: int or float,
            y: int or float
    ):
        self.x = x
        self.y = y


    def __str__(self):
        return f"x: {self.x}; y: {self.y};"



class Vector2D  :

    start: Point2D
    end: Point2D

    def __init__(
            self,
            start: Point2D,
            end: Point2D
    ):
        self.start = start
        self.end = end


    def __add__(self, other_vector: Vector2D):
        return (
            Vector2D(
            Point2D(Vector2D.start.x + other_vector.start.x, Vector2D.start.y + other_vector.start.y),
            Point2D(Vector2D.end.x + other_vector.end.x, Vector2D.end.y + other_vector.end.y))
        )


    def __sub__(self, other_vector: Vector2D):
        return (
            Vector2D(
            Point2D(Vector2D.start.x - other_vector.start.x, Vector2D.start.y - other_vector.start.y),
            Point2D(Vector2D.end.x - other_vector.end.x, Vector2D.end.y - other_vector.end.y))
        )



    def __mul__(self, number: int or float):
        return (
            Vector2D
            (Point2D(self.start.x, self.start.y * number),
             Point2D(self.end.x, self.end.y * number))
        )


    def __len__(self):
        st1 = self.end.x - self.start.x
        st2 = self.end.y - self.start.y

        return (st1**2 + st2**2)**0.5


    def __str__(self):
        return f"Start point: {self.start}; End point: {self.end};"


# 2

class Money:

    dollars: int
    cents: int

    def __init__(
            self,
            dollars: int,
            cents: int
    ):
        self.dollars = dollars + cents // 100
        self.cents = cents % 100


    def __add__(self, new_money: Money):
        new_dollars = self.dollars + new_money.dollars + new_money.cents // 100
        new_cents = self.cents + new_money.cents % 100

        return Money(new_dollars, new_cents)


    def __sub__(self, new_money: Money):
        new_dollars = self.dollars - new_money.dollars - new_money.cents // 100
        new_cents = self.cents - new_money.cents % 100

        return Money(new_dollars, new_cents)


    def __str__(self):
        return f"Dollars: {self.dollars}; Cents: {self.cents};"


# 3

class Time:

    hours: int
    minutes: int
    seconds: int or float

    def __init__(
            self,
            hours: int,
            minutes: int,
            seconds: int or float
    ):
        self.hours = hours + minutes // 60
        self.minutes = minutes % 60 + seconds // 60
        self.seconds = seconds % 60


    def __add__(self, other_time: Time):
        new_hours = self.hours + other_time.hours + other_time.minutes // 60
        new_minutes = self.minutes + other_time.minutes % 60 + other_time.seconds // 60
        new_seconds = self.seconds + other_time.seconds % 60

        return Time(new_hours, new_minutes, new_seconds)


    def __len__(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds


    def __str__(self):
        return f"Hours: {self.hours}; Minutes: {self.minutes}; Seconds: {self.seconds};"


# 4

class Point:

    x: int or float
    y: int or float

    def __init__(
            self,
            x: int or float,
            y: int or float
    ):
        self.x = x
        self.y = y


    def __add__(self, other_point: Point):
        return Point(self.x + other_point.x, self.y + other_point.y)


    def __sub__(self, other_point: Point):
        return Point(self.x - other_point.x, self.y - other_point.y)


    def __str__(self):
        return f"x: {self.x}; y: {self.y};"


# 5

class ColoredPoint(Point):

    color: str

    def __init__(self, x, y, color: str):
        super().__init__(x, y)
        self.color = color


    def __add__(self, other_point: ColoredPoint):
        new_color = "black"

        if self.color == other_point.color:
            new_color = self.color

        return ColoredPoint((self.x + other_point.x), (self.y + other_point.y), new_color)
    
    
    def __str__(self):
        return f"x: {self.x}; y: {self.y}; color: {self.color};"


# 6

class Matrix:

    a: int or float
    b: int or float
    c: int or float
    d: int or float

    def __init__(
            self,
            a: int or float,
            b: int or float,
            c: int or float,
            d: int or float
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    def __add__(self, other_matrix: Matrix):
        return (
            Matrix(
                self.a + other_matrix.a,
                self.b + other_matrix.d,
                self.c + other_matrix.c,
                self.d + other_matrix.d
                ))


    def __mul__(self, other_matrix: Matrix):
        return (
            Matrix(
                self.a * other_matrix.a,
                self.b * other_matrix.d,
                self.c * other_matrix.c,
                self.d * other_matrix.d
            ))


    def __len__(self):
        return 4


    def __str__(self):
        return f"{self.a} {self.b}\n{self.c} {self.d}"