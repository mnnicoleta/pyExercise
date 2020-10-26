# We started a company that builds Polygons.
# Our first two products are:
# • triangles
# • squares
# Requirements:
# 1. Be able to create Polygons with n sides ( 3 sides -> triangle, 4 -> sides square, …, n sides)
# 2. Display the number of sides of the Polygon when we print any Polygon object
# 3. Display the values of each side for all Polygon objects
# • Side 1 with length: 2
# • Side 2 with length: 4
# • Side 3 with length: 6
# 4. Compute area for Triangles and Squares
# Definitions:
# 1. A polygon is a geometrical figure with 3 or more sides
# 2. Triangle area = s(s-a)(s-b)(s-c) ** 0.5 where s = (a+b+c) / 2 and a,b,c are the length
# of the sides
# 3. Square area = width * length
from math import sqrt


class Polygons(object):
    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class Triangle(Polygons):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return (s_p * (s_p - s1) * (s_p - s2) * (s_p - s3)) ** 0.5


class SquarePlaceholderMixin(Polygons):

    def __init__(self, area):
        one_side = sqrt(area)
        print('treceeee')
        super().__init__(one_side, one_side, one_side, one_side)


class Square(SquarePlaceholderMixin, Polygons):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side, *_ = self.sides
        return side ** 2


print('Triangle 1')
triangle1 = Triangle(1, 2, 3)
triangle1.display()

print("Square 1")
square1 = Square(3, 3, 3, 3)
square1.display()

print('Second square')
square2 = Square(4, 4, 4, 4)
square2.area()
square2.display()

print('Create a square no 3 giving the area')
square3 = Square(25)
square3.display()
print(type(square3))

# https://platforma.scoalainformala.ro/course/view.php?id=848
# 6 Challenge:
# We have new customers for our Polygons company.
# • They need to create square objects with a certain area
# • They need a method to compute the perimeter only for triangle objects
# Requirements: * add an alternative constructor to Square class that takes the area as an argument
# and creates a square object with the appropriate sides
# Example :
# sq = Square.from_area(8)
# print(sq)
# Side 1 with length: 2
# Side 2 with length: 4
# Side 3 with length: 2
# Side 4 with length: 4
# • we want to make our perimeter method also available to other shapes in the future. Create
# a mixin class for perimeter that contains the perimeter method
