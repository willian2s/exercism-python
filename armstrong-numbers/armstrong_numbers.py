def is_armstrong_number(number):
    """Check if the number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits each
    raised to the power of the number of digits.

    :param number: int - number to check.
    :return: bool - whether the number is an Armstrong number or not.
    """

    number_str = str(number)
    number_of_digits = len(number_str)

    return number == sum(int(digit) ** number_of_digits
                         for digit in number_str)
