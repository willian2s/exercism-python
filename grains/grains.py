total_grains = 0
grains_on_square = 1


def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains_on_square = 1
    for _ in range(number - 1):
        grains_on_square *= 2
    return grains_on_square


def total():
    total_grains = 0
    grains_on_square = 1
    for _ in range(64):
        total_grains += grains_on_square
        grains_on_square *= 2
    return total_grains
