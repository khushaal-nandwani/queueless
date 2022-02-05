from Seat import Seat


class Table:
    """
    size: the number of seats a table can have
    """

    occupied: bool
    size: int

    def __init__(self):
        self.size = 2
        self.occupied = False

