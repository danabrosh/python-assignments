import math
import sys

if len(sys.argv) != 2:
    sys.exit(f"Usage: {sys.argv[0]} RADIUS")

circle_radius = float(sys.argv[1])
area = math.pi * circle_radius ** 2
circumference = 2 * math.pi * circle_radius
print("The area of the circle is: ", area)
print("The circumference of the circle is: ", circumference)
