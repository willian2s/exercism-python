"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created: int = 0
    x_coordinate: int = 0
    y_coordinate: int = 0
    health: int = 0

    def __init__(self, *location):
        Alien.total_aliens_created += 1
        self.health = 3
        self.x_coordinate = location[0]
        self.y_coordinate = location[1]

    def hit(self):
        """
        Decreases the health of the object by 1.
        """
        self.health -= 1

    def is_alive(self):
        """
        Check if the object is alive based on its health attribute.
        No parameters.
        Returns a boolean indicating if the object is alive.
        """
        if self.health > 0:
            return True
        return False

    def teleport(self, *position):
        """
        Set the x and y coordinates of the object to the provided position.
        """
        self.x_coordinate = position[0]
        self.y_coordinate = position[1]

    def collision_detection(self, obj):
        """
        Perform collision detection for the given object.

        Args:
            obj: The object for which collision detection needs to be performed.

        Returns:
            None
        """


def new_aliens_collection(start_positions):
    """
    Creates a list of Alien objects and returns it.
    """
    aliens = [Alien(x_cord, y_cord) for x_cord, y_cord in start_positions]
    return aliens
