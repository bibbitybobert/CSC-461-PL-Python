import book_robert.Boat.BoatBehavior as bb


class Boat:
    def __init__(self, boat_id: int, power: int):
        self.char = '⛴'
        self.id = boat_id
        self.power = power
        self.behavior = None
        self.speed = 1

    def __str__(self):
        return self.char

    def update(self):
        return self.power

    def setBehavior(self, behavior):
        self.behavior = bb.steady if behavior == 1 else bb.max_dist
