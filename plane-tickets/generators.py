"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    seat_letters = ["A", "B", "C", "D"]

    complete_row = number // 4

    remaining_seate = number % 4

    for _ in range(complete_row):
        for letter in seat_letters:
            yield letter

    for i in range(remaining_seate):
        yield seat_letters[i]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    row = 1
    seat_letters = ["A", "B", "C", "D"]

    for _ in range(number):
        if row == 13:
            row += 1

        seat_letter = seat_letters[_ % 4]
        seat = f"{row}{seat_letter}"

        if _ % 4 == 3:
            row += 1

        yield seat


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_generator = generate_seats(len(passengers))
    seat_assignments = {}

    for passenger in passengers:
        seat_assignments[passenger] = next(seat_generator)

    return seat_assignments


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        _, row, seat_letter = int(
            seat_number[:-1]), int(seat_number[:-1]), seat_number[-1]
        ticket_id = f"{row}{seat_letter}{flight_id}"
        ticket_id = ticket_id.ljust(12, '0')

        yield ticket_id
