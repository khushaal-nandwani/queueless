class Table:
    """
    size: the number of seats a table can have
    """

    occupied: bool
    size: int

    def __init__(self, size):
        self.size = size
        self.occupied = False

