from math import pi


def welcome():
    print('''
==================
Area Calculator 📐
==================
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit
''')
    choice = int(input("Choose a shape to calculate the area (1-5): "))
    return choice


def square():
    a = float(input("Enter the length of a side: "))
    area = a**2
    return area


def rectangle():
    li = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    area = li * w
    return area


def triangle():
    b = float(input("Enter the base: "))
    h = float(input("Enter the height: "))
    area = 0.5 * b * h
    return area


def circle():
    r = float(input("Enter the radius: "))
    area = pi * r**2
    return area


def main():
    while True:
        choice = welcome()
        if choice == 1:
            area = triangle()
            print(f"The area of the triangle is: {area}")
        elif choice == 2:
            area = rectangle()
            print(f"The area of the rectangle is: {area}")
        elif choice == 3:
            area = square()
            print(f"The area of the square is: {area}")
        elif choice == 4:
            area = circle()
            print(f"The area of the circle is: {area}")
        elif choice == 5:
            print("Thank you for using the Area Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
