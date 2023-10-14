import math

def calculate_circle_area(radius):
    return math.pi * (radius**2)

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

choice = input("Enter shape (circle/rectangle/triangle): ").lower()

if choice == "circle":
    radius = float(input("Enter the radius: "))
    area = calculate_circle_area(radius)
    perimeter = calculate_circle_perimeter(radius)
elif choice == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)
elif choice == "triangle":
    base = float(input("Enter the base length: "))
    height = float(input("Enter the height: "))
    area = calculate_triangle_area(base, height)
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
else:
    print("Invalid choice!")

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
