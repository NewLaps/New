class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(7)
square1 = Rectangle(8,4)
print(square.calculate_area())
print(square1.calculate_area())
