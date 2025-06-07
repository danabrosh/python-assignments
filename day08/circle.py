from circle_utils import calculate_area, calculate_circumference

def main():
    circle_radius = float(input("What is the radius of the circle? "))
    area = calculate_area(circle_radius)
    circumference = calculate_circumference(circle_radius)
    print("The area of the circle is: ", area)
    print("The circumference of the circle is: ", circumference)

if __name__ == "__main__":
    main()
