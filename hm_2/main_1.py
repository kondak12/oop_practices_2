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


    def add(self, other_vector: Vector2D):
        return (
            Vector2D(
            Point2D(Vector2D.start.x + other_vector.start.x, Vector2D.start.y + other_vector.start.y),
            Point2D(Vector2D.end.x + other_vector.end.x, Vector2D.end.y + other_vector.end.y))
        )


    def sub(self, other_vector: Vector2D):
        return (
            Vector2D(
            Point2D(Vector2D.start.x - other_vector.start.x, Vector2D.start.y - other_vector.start.y),
            Point2D(Vector2D.end.x - other_vector.end.x, Vector2D.end.y - other_vector.end.y))
        )



    def mul(self, number: int or float):
        return (
            Vector2D
            (Point2D(self.start.x, self.start.y * number),
             Point2D(self.end.x, self.end.y * number))
        )


    def len(self):
        st1 = self.end.x - self.start.x
        st2 = self.end.y - self.start.y

        return (st1**2 + st2**2)**0.5