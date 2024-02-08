"""
Calculate collatz conjecture
"""


def steps(number):
    """
    Calculate the number of steps required to reach 1 in the Collatz conjecture
    for the given number.

    Parameters:
    number (int): The input positive integer

    Returns:
    int: The number of steps required to reach 1 in the Collatz conjecture
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return 0
    if number % 2 == 0:
        return 1 + steps(number // 2)
    return 1 + steps(3 * number + 1)
