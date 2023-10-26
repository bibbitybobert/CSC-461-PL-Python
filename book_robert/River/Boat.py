class Boat:
    def __init__(self, boat_id: int, power: int, behavior: int = 0):
        self.char = '⛴'
        self.id = boat_id
        self.power = power

    def __str__(self):
        return self.char
