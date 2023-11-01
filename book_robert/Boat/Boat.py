import book_robert.Boat.BoatBehavior as bb


globl_boat_id = 1  # Global boat ID that does not reset unless program is re compiled


class Boat:
    """
    class for the boats that pass through the River
    """
    def __init__(self, power: int):
        """
        function to initialize this class with default values and set engine power
        :param power: engine power of the boat
        """
        global globl_boat_id
        self.char = '⛴'
        self.id = globl_boat_id
        self.power = power
        self.behavior = None
        self.speed = 1
        globl_boat_id += 1

    def __str__(self):
        """
        overridden string function to return the char of the boat
        :return: boat ASCII char
        """
        return self.char

    def setBehavior(self, behavior):
        """
        sets the behavior of the boat (1 for steady, 2 for max)
        :param behavior: int value for behavior of the boat
        :return: Nothing
        """
        self.behavior = bb.steady if behavior == 1 else bb.max_dist


