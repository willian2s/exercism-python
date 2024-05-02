"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(minutes_in_oven: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    result = EXPECTED_BAKE_TIME - minutes_in_oven
    return result


def preparation_time_in_minutes(layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers
    :return: int - preparation time in minutes

    This function takes the number of layers you want to add to the lasagna
    and returns how many minutes you would spend making them.
    """
    result = layers * 2
    return result


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time in minutes.

    :param layers: int - number of layers
    :param elapsed_bake_time: int - baking time already elapsed
    :return: int - elapsed time in minutes

    Function that takes the number of layers you've added to the lasagna
    and the elapsed time in minutes since the lasagna was first
    baked and returns how many minutes you've worked on the lasagna
    so far.
    """
    preparation_time = preparation_time_in_minutes(layers)
    result = preparation_time + elapsed_bake_time
    return result
