from book_robert.Boat import Boat as b
from book_robert.Iterator import Iterator as it
from book_robert.Boat import BoatBehavior as bb
from book_robert.River import LockBehavior as lb


class RiverPart:
    def __init__(self):
        self.boat_num = 0


class Section(RiverPart):
    def __init__(self, size: int, flow: int):
        super().__init__()
        self.flow = flow
        self.subsec = []
        for i in range(0, size):
            self.subsec.append(SubSec(i))

    def __iter__(self):
        return it.Iterator(self.subsec)

    def __str__(self):
        out_str = ''
        for sstr in self:
            out_str = str(sstr) + out_str
        return out_str

    def str2(self):
        out_str = ''
        for bstr in self:
            out_str = bstr.str2() + out_str
        return out_str

    def add_boat(self, boat_id: int, power: int, method: int):
        if not self.subsec[0].has_boat:
            new_boat = b.Boat(boat_id, power)
            new_boat.setBehavior(method)
            new_boat.speed = new_boat.behavior(power, self.flow)
            self.subsec[0].add_boat(new_boat)
            self.boat_num += 1

    def returns_boat(self):
        if self.subsec[-1].has_boat:
            return self.subsec[-1].boat
        return None

    def update(self):
        for s in self:
            moving_boat = s.returns_boat()
            if moving_boat is not None:
                next_loc = moving_boat.behavior(moving_boat.power, self.flow) + s.addr
                if next_loc < len(self.subsec):
                    self.subsec[next_loc].add_boat(moving_boat)
                elif s.addr != len(self.subsec):
                    self.subsec[-1].add_boat(moving_boat)
                s.remove_boat()

    def print_deets(self):
        return 'Boats: ' + str(self.boat_num) + ' Flow: ' + str(self.flow)

    def can_accept(self):
        if not self.subsec[0].has_boat:
            return True
        return False

    def import_boat(self, boat: b.Boat):
        self.subsec[0].add_boat(boat)
        self.subsec[0].boat.speed = boat.behavior(boat.power, self.flow)


class SubSec:
    def __init__(self, loc):
        self.char = '〜〜〜'
        self.bot = '〜〜〜'
        self.has_boat = False
        self.boat = None
        self.addr = loc

    def add_boat(self, boat: b.Boat):
        self.has_boat = True
        self.boat = boat
        self.char = boat.char + '〜〜'
        self.bot = str(boat.id) + '〜〜'

    def remove_boat(self):
        self.has_boat = False
        self.boat = None
        self.char = self.char = '〜〜〜'
        self.bot = '〜〜〜'

    def __str__(self):
        return self.char

    def str2(self):
        return self.bot

    def returns_boat(self):
        if self.has_boat:
            return self.boat
        else:
            return None



class Lock(RiverPart):
    def __init__(self, depth: int):
        super().__init__()
        self.depth = depth
        self.curr = 0
        self.top_char = list(['_', 'X', '(', ' ', str(self.curr), ')', '_'])
        self.bot_char = list(['.'] * 7)
        self.behavior = None
        self.boat = None

    def import_boat(self, boat: b.Boat):
        self.boat = boat
        self.boat_num = 1
        self.top_char[1] = boat.char
        self.bot_char[1] = str(boat.id)

    def set_behavior(self, behavior: int):
        if behavior == 1:
            self.behavior = lb.pass_through
        elif behavior == 2:
            self.behavior = lb.basic
        else:
            self.behavior = lb.fast

    def __str__(self):
        self.top_char[4] = str(self.curr)
        return ''.join(self.top_char)

    def str2(self):
        return ''.join(self.bot_char)

    def returns_boat(self):
        if self.boat_num == 1 and self.curr + 1 >= self.depth:
            return self.boat
        else:
            return None

    def exit_boat(self):
        self.boat = None
        self.boat_num = 0
        self.top_char[1] = 'X'
        self.bot_char[1] = '.'

    def update(self):
        if self.boat is not None:
            if self.curr == self.depth:
                self.exit_boat()
            elif self.curr + 1 == self.depth:
                self.curr += self.behavior('Fill')
                self.exit_boat()
            else:
                self.curr += self.behavior('Fill')
        else:
            if self.curr > 0:
                self.curr -= self.behavior('Drain')

    def can_accept(self):
        return True if self.curr == 0 and self.boat_num ==0 else False
