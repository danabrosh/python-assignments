from math import pi

def calculate_area(radius):
    """
    Returns the area of a circle given its radius.
    
    Examples:
        >>> calculate_area(2)
        12.566370614359172
        >>> calculate_area(1)
        3.141592653589793
    """
    return pi * radius ** 2

def calculate_circumference(radius):
    """
    Returns the circumference of a circle given its radius.
    
    Examples:
        >>> calculate_circumference(2)
        12.566370614359172
        >>> calculate_circumference(1)
        6.283185307179586
    """
    return 2 * pi * radius
