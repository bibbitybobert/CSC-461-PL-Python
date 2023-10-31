import book_robert.Boat.BoatBehavior as bb


globl_boat_id = 1
class Boat:
    def __init__(self, power: int):
        global globl_boat_id
        self.char = '⛴'
        self.id = globl_boat_id
        self.power = power
        self.behavior = None
        self.speed = 1
        globl_boat_id += 1

    def __str__(self):
        return self.char

    def update(self):
        return self.power

    def setBehavior(self, behavior):
        self.behavior = bb.steady if behavior == 1 else bb.max_dist
