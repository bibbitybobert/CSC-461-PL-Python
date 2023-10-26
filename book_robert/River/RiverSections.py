import Boat as b
class RiverPart:
    def update(self):
        print('update')


class Section(RiverPart):
    def __init__(self, flow: int):
        self.flow = flow
        self.boat = False
        self.top_char = '〜〜〜'
        self.bot_char = '〜〜〜'

    def add_boat(self, boat_id: int, power: int = 1):
        self.boat = b.Boat(boat_id, power)
        self.top_char = self.boat.char + '〜〜'
        self.bot_char = str(self.boat.id) + '〜〜'

    def __str__(self):
        return self.top_char


class Lock(RiverPart):
    def __init__(self, behavior: int, depth: int):
        self.behavior = behavior
        self.depth = depth
        self.boat = False
        self.top_char = '_X( ' + str(self.depth) + ')_'
        self.bot_char = '.......'

    def add_boat(self, boat_id: int, power: int = 1):
        self.boat = b.Boat(boat_id, power)
        self.top_char = '_' + self.boat.char + '( ' + str(self.depth) + ')_'
        self.bot_char = str(self.boat.id) + '......'

    def __str__(self):
        return self.top_char
