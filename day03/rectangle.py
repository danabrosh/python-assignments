import sys

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} HEIGHT WIDTH")

rectangle_height = float(sys.argv[1])
rectangle_width = float(sys.argv[2])
rectangle_area = rectangle_height * rectangle_width
print("The area of the rectangle is: ", rectangle_area)
rectangle_perimeter = 2 * (rectangle_height + rectangle_width)
print("The perimeter of the rectangle is: ", rectangle_perimeter)
