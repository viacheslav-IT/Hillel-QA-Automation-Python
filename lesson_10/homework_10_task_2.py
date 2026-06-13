# Task 2

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return self.__side * 4

    def __str__(self):
        return 'Square'


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def __str__(self):
        return 'Rectangle'


square = Square(4)
rectangle = Rectangle(4, 5)


for i in (square, rectangle):
    print(f'{i}: area {i.area()}, perimeter {i.perimeter()}')