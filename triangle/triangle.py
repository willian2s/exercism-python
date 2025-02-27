def equilateral(sides):
    a, b, c = sides

    if is_triangle(sides):
        if a == b == c:
            return True
        else:
            return False
    else:
        return False

def isosceles(sides):
    a, b,c = sides

    if is_triangle(sides):
        if a == b or a == c or b == c:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    a, b,c = sides

    if is_triangle(sides):
        if a != b and a != c and b != c:
            return True
        else:
            return False
    else:
        return False

def is_triangle(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b >= c and a + c >= b and b + c >= a:
        return True
    else:
        return False
