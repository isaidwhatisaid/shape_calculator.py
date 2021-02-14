# Class that does things with rectangles
class Rectangle:

    # Constructor method taking width and height arguments
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # String representation method
    def __str__(self):
        return 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) + ')'
    
    # Method to set a new width
    def set_width(self, width):
        self.width = width
    
    # Method to set a new height
    def set_height(self, height):
        self.height = height
    
    # Method to get area
    def get_area(self):
        return (self.width*self.height)
    
    # Method to get perimeter
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    
    # Method to get diagonal length
    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)
    
    # Method to print a picture of the shape using * symbols
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        row_length = '*'*self.width + '\n'
        picture = row_length*self.height
        return picture
    
    # Method to check how many times the passed shape will fit inside the main shape
    def get_amount_inside(self, shape):
        width_num = int(self.width / shape.width - (self.width % shape.width / shape.width))
        height_num = int(self.height / shape.height - (self.height % shape.height / shape.height))
        if width_num < 1 or height_num < 1:
            return 0
        return width_num*height_num

# Square class that inherits rectangle methods
class Square(Rectangle):

    # Constructor method that takes on length and applies that value to both the width and height values of the rectangle class
    def __init__(self, length):
        self.width = self.height = self.length = length
    
    # String method for squares
    def __str__(self):
        return 'Square(side=' + str(self.length) + ')'
    
    # Methods to set length of all sides
    def set_side(self, length):
        self.width = self.height = self.length = length
    def set_width(self, length):
        self.width = self.height = self.length = length
    def set_height(self, length):
        self.width = self.height = self.length = length

# Testers
rect = Rectangle(15,10)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(10)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_area())
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))