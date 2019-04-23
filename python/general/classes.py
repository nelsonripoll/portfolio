class Rectangle():
    """A simple shape class"""

    def __init__(self, length, width):
        """Initialize a rectangle with length and width"""
        self.length = length
        self.width  = width

    def get_area(self):
        return self.length * self.width

    def get_parameter(self):
        return (self.length * 2) + (self.width * 2)

    def is_square(self):
        return self.length == self.width


class Square(Rectangle):
    def __init__(self, side):
        """Initialize a square with length and width set to side"""
        super().__init__(side, side)

# python 2.7
# class Square(Rectangle):
#     def __init__(self, side):
#         """Initialize a square with length and width set to side"""
#         super(Square, self).__init__(side, side)

new_shape = Rectangle(2, 3)
new_shape.get_area()      # 6
new_shape.get_parameter() # 10
new_shape.is_square()     # False

another_shape = Square(2)
new_shape.get_area()      # 4
new_shape.get_parameter() # 8
another_shape.is_square() # True
