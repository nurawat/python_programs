# Python Program for Program to find area of a circle
# Area of a circle can simply be evaluated using following formula.
# Area = pi * r2
# where r is radius of circle 


def area(radius):
  return 3.14 * (radius * radius)

radius = float(input("Enter the Radius of the number: "))
print("Area is %.6f" % area(radius));
