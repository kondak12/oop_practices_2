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