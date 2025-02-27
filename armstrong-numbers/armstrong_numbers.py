def is_armstrong_number(number):
    if number < 0:
        return False
    if number == 0:
        return True

    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == number

