# shapes.py

import math

# Area of Circle
def area_circle(radius):
    return math.pi * radius * radius

# Area of Rectangle
def area_rectangle(length, width):
    return length * width

# Area of Triangle
def area_triangle(base, height):
    return 0.5 * base * height

# main.py

import shapes

print("Choose Shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle:", shapes.area_circle(r))

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", shapes.area_rectangle(l, w))

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of Triangle:", shapes.area_triangle(b, h))

else:
    print("Invalid choice!")