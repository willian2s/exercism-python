"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of lasagna layers to prepare.

    Returns:
        int: The total preparation time (in minutes) derived from
        'PREPARATION_TIME' multiplied by the number of layers.

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    """

    return number_of_layers * PREPARATION_TIME


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed time in minutes.

    Parameters:
        number_of_layers (int): The number of lasagna layers prepared.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed time (in minutes), calculated as the sum of
        the preparation time and the time already spent baking.

    Function that takes the number of layers and the elapsed baking time as
    arguments and returns the sum of the preparation time and the time the
    lasagna has already been in the oven.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)

    return preparation_time + elapsed_bake_time
