


"""
  Вам необходимо реализовать векторную алгебру, создав свой класс Vector. 
  Из необходимого минимума для реализации: 
        взятие нормы вектора, 
        умножение вектора на число, 
        сложение, 
        скалярное и 
        векторное произведения двух векторов.         
"""

import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x, self.y, self.z = x, y, z

    # для итерации по координатам (можно использовать в конструкциях for in self)
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    # взятие нормы вектора (она же длина вектора)
    def norm(self):
        return math.sqrt(sum(value**2 for value in self))

    # векторное произведение векторов через класс-метод
    @classmethod
    def mul_vectors(cls, a, b):
        return Vector(a.y * b.z - a.z * b.y,
                      a.z * b.x - a.x * b.z,
                      a.x * b.y - a.y * b.x)

    # скалярное произведение векторов
    @classmethod
    def mul_scalar(cls, a, b):
        return sum([a*b for a, b in zip(a, b)])

    # умножение вектора на число и вектор на вектор (векторно) через "магический" метод
    def __mul__(self, other):
        if isinstance(other, Vector):  # вектор на вектор
            return Vector.mul_vectors(self, other)
        else:   # число на вектор
            return Vector(*map(lambda a: a*other, self))

    # скалярное произведние через &
    def __and__(self, other):
        if isinstance(other, Vector):  # вектор на вектор
            return Vector.mul_scalar(self, other)
        else:   # вектор & число (поэлементно)
            return Vector(*map(lambda a: a & other, self))

    # число на вектор когда, число справа
    def __rmul__(self, other):
        return self * other

    # сложение
    def __add__(self, other):
        if isinstance(other, Vector):  # вектор + вектор
            return Vector(*[a+b for a, b in zip(self, other)])
        else:  # вектор + число
            return Vector(*map(lambda a: a + other, self))

    # вычитание
    def __sub__(self, other):
        if isinstance(other, Vector):  # Вектор + вектор
            return Vector(*[a-b for a, b in zip(self, other)])
        else:  # вектор - число (поэлементно)
            return Vector(*map(lambda a: a-other, self))

    # деление поэлементно
    def __div__(self, other):
        return Vector(*[a/b for a, b in zip(self, other)])

    # деление по модулю поэлементно
    def __mod__(self, other):
        return Vector(*[a % b for a, b in zip(self, other)])

    #  смена знака
    def __neg__(self):
        return Vector(*map(lambda a: -a, self))

    # cравнение
    def __eq__(self, other):
        return all([a == b for a, b in zip(self, other)])

    # вывод 
    def __repr__(self):
        return f"Vector{tuple(self)}"


if __name__ == "__main__":
    a = Vector(1, 2, 3)

    b = Vector(2, 1, -2)
    c = Vector(3, 4)

    d = Vector(1, 2, -5)
    e = Vector(4, 8, 1)

    """ Используем assert для проверки правильности работы нашего класса, 
        если провека не прошла будет AssertionError 
    """

    # Норма вектора
    assert(c.norm() == 5)

    # вектор + число
    assert(a + 2 == Vector(3, 4, 5))

    # вектор - число
    assert(a - 2 == (-1, 0, 1) ) 

    # Умножение на число
    assert(a * 2 == Vector(2, 4, 6))
    assert(2 * b == Vector(4, 2, -4))

    # Векторное произведение
    assert(Vector.mul_vectors(a, b) == Vector(-7, 8, -3))
    assert(a * b == Vector(-7, 8, -3))

    # Скалярное произведение, используем & для сокращенной записи
    assert(Vector.mul_scalar(d, e) == 15)
    assert(d & e == 15)

    # Cложение векторов
    assert(a + b == Vector(3, 3, 1))

    # Вычитание векторов
    assert(a - b == Vector(-1, 1, 5))
    
    # Смена знака
    assert(-a == Vector(-1, -2, -3))
    
    print("Проверено")


# In[ ]:




