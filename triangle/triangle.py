"""
Get the length of each side of a triangle and check if it forms a valid triangle.
"""


def check_triangle(side):
    """
    Check if the given sides form a valid triangle.

    Parameters:
    - side1, side2, side3 (int): Lengths of the sides of the triangle.

    Returns:
    - bool: True if the sides form a valid triangle, False otherwise.
    """
    side1, side2, side3 = side
    return (
        side1 > 0 and
        side2 > 0 and
        side3 > 0 and
        side1 + side2 > side3 > 0 and
        side2 + side3 > side1 > 0 and
        side1 + side3 > side2 > 0
    )


def equilateral(sides):
    """
    Check if the given sides form an equilateral triangle.

    Parameters:
    sides (list): A list of three side lengths of the triangle.

    Returns:
    bool: True if the sides form an equilateral triangle, False otherwise.
    """
    if check_triangle(sides) is False:
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    """
    Check if the given sides form an isosceles triangle.

    Args:
        sides (list): A list of three integers representing the lengths of the sides of a triangle.

    Returns:
        bool: True if the sides form an isosceles triangle, False otherwise.
    """
    if check_triangle(sides) is False:
        return False
    a, b, c = sides
    return a == b or a == c or b == c


def scalene(sides):
    """
    A function to determine if a triangle is scalene based on its sides.
    Parameter:
        sides: a list of three integers representing the sides of the triangle.
    Return type:
        boolean indicating whether the triangle is scalene or not.
    """
    if check_triangle(sides) is False:
        return False
    a, b, c = sides
    if a == b or a == c or b == c:
        return False
    if a != b != c:
        return True
