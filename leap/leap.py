"""
This is the leap exercise
"""


def leap_year(year):
    """
    Determine whether a year is a leap year.
    :param year: int, the year to be checked
    :return: bool, whether the year is a leap year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
