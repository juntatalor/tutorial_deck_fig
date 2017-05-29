import math


class Fig:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y


class Circle(Fig):
    """
    >>> c = Circle(5, 6, 10)
    >>> c.square()
    314.1592653589793
    >>> c.perim()
    62.83185307179586
    """

    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def square(self):
        return math.pi * self.r ** 2

    def perim(self):
        return 2 * math.pi * self.r


class Rect(Fig):
    """
    >>> r = Rect(1, 6, 60, 5)
    >>> r.square()
    300
    >>> r.perim()
    130
    """

    def __init__(self, x, y, w, l):
        super().__init__(x, y)
        self.w = w
        self.l = l

    def square(self):
        return self.w * self.l

    def perim(self):
        return 2 * (self.w + self.l)


class Square(Rect):
    """
    >>> s = Square(4, 7, 10)
    >>> s.square()
    100
    >>> s.perim()
    40
    >>> s.get_coord()
    (4, 7)
    """

    def __init__(self, x, y, w):
        super().__init__(x, y, w, w)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
