from math import sqrt


class Square:

    def __init__(self, side):
        self._side = None
        self._perimeter = None
        self._area = None
        self._diagonal = None
        self._set_square_values(side)

    def _set_square_values(self, side):
        self._side = side
        self._perimeter = 4 * side
        self._area = side * side
        self._diagonal = sqrt(2) * side

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_side):
        self._set_square_values(new_side)

    def set_perimeter(self, new_perimeter):
        new_side = new_perimeter / 4
        self._set_square_values(new_side)

    def set_area(self, new_area):
        new_side = sqrt(new_area)
        self._set_square_values(new_side)

    def set_diagonal(self, new_diagonal):
        new_side = new_diagonal / sqrt(2)
        self._set_square_values(new_side)

    @property
    def side(self):
        return self.get_side()

    @property
    def perimeter(self):
        return self.get_perimeter()

    @property
    def area(self):
        return self.get_area()

    @property
    def diagonal(self):
        return self.get_diagonal()

    @side.setter
    def side(self, new_side):
        self._set_square_values(new_side)

    @perimeter.setter
    def perimeter(self, new_perimeter):
        new_side = new_perimeter / 4
        self._set_square_values(new_side)

    @area.setter
    def area(self, new_area):
        new_side = sqrt(new_area)
        self._set_square_values(new_side)

    @diagonal.setter
    def diagonal(self, new_diagonal):
        new_side = new_diagonal / sqrt(2)
        self._set_square_values(new_side)


square = Square(11)

print(square.get_side())  # 11
print(square.side)        # 11
print(square.perimeter)   # 44

square.perimeter = 48

print(square.get_side())  # 12
print(square.side)        # 12
print(square.perimeter)   # 48
