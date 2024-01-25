"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # Calculate the true average
    true_average = card_average(hand)

    # Calculate the average of the first and last index values
    first_last_average = (hand[0] + hand[-1]) / 2

    # Calculate the average of the middle card (if the hand has an odd number of cards)
    middle_index = len(hand) // 2
    middle_average = hand[middle_index] if len(hand) % 2 == 1 else 0

    # Check if either of the approximate averages equals the true average
    return true_average in (first_last_average, middle_average)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    # Calculate the average of even indexed card values
    even_average = sum(hand[::2]) / len(hand[::2])

    # Calculate the average of odd indexed card values
    odd_average = sum(hand[1::2]) / len(hand[1::2])

    # Check if the even and odd averages are equal
    return even_average == odd_average


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    last_index = -1
    if hand[last_index] == 11:
        hand[last_index] = 22
    return hand
