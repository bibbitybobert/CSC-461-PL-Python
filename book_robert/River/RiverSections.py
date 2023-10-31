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
        self.size = size
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

    def add_boat(self, power: int, method: int):
        new_boat = b.Boat(power)
        if not self.subsec[0].has_boat:
            new_boat.setBehavior(method)
            new_boat.speed = new_boat.behavior(power, self.flow)
            self.subsec[0].add_boat(new_boat)
            self.boat_num += 1

    def returns_boat(self):
        if self.subsec[-1].has_boat:
            self.boat_num -= 1
            return self.subsec[-1].boat
        return None

    def update(self, return_boat):
        for s in self:
            moving_boat = s.returns_boat()
            if moving_boat is not None:
                movement = moving_boat.behavior(moving_boat.power, self.flow)
                if movement + s.addr < len(self.subsec):
                    next_loc = s.addr + movement
                    for j in range(1, movement):
                        if self.subsec[s.addr + j].has_boat:
                            next_loc = s.addr + j - 1
                            break
                    self.subsec[next_loc].add_boat(moving_boat)
                elif s.addr != self.size - 1:
                    next_loc = -1
                    for j in range(1, self.size - s.addr):
                        if self.subsec[s.addr + j].has_boat:
                            next_loc = s.addr + j - 1
                            break
                    self.subsec[next_loc].add_boat(moving_boat)
                if s.addr != self.size - 1 or return_boat:
                    s.remove_boat()

    def print_deets(self):
        return 'Boats: ' + str(self.boat_num) + ' Flow: ' + str(self.flow) + '\n'

    def can_accept(self):
        if not self.subsec[0].has_boat:
            return True
        return False

    def import_boat(self, boat: b.Boat):
        self.subsec[0].add_boat(boat)
        self.subsec[0].boat.speed = boat.behavior(boat.power, self.flow)
        self.boat_num += 1


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
        self.char = boat.char.ljust(3, '〜')
        self.bot = str(boat.id).ljust(3, '〜')

    def remove_boat(self):
        self.has_boat = False
        self.boat = None
        self.char = '〜〜〜'
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
        self.top_char = '_X(' + str(self.curr).rjust(2) +  ')_'
        self.bot_char = '.' * 7
        self.behavior = None
        self.boat = None

    def import_boat(self, boat: b.Boat):
        self.boat = boat
        self.boat_num = 1
        self.top_char = '_' + self.boat.char + '(' + str(self.curr).rjust(2) + ')_'
        self.bot_char = str(boat.id).ljust(2, '.') + self.bot_char[2:]

    def set_behavior(self, behavior: int):
        if behavior == 1:
            self.behavior = lb.pass_through
        elif behavior == 2:
            self.behavior = lb.basic
        else:
            self.behavior = lb.fast

    def __str__(self):
        self.top_char = self.top_char[0:3] + str(self.curr).rjust(2) + self.top_char[5:]
        return self.top_char

    def str2(self):
        return self.bot_char

    def returns_boat(self):
        if self.boat_num == 1 and self.curr + 1 >= self.depth:
            return self.boat
        else:
            return None

    def exit_boat(self):
        self.boat = None
        self.boat_num = 0
        self.top_char = '_X(' + str(self.curr).rjust(2) + ')_'
        self.bot_char = '..' + self.bot_char[2:]

    def update(self, return_boat):
        if self.boat is not None:
            if return_boat:
                if self.curr == self.depth:
                    self.exit_boat()
                elif self.curr + 1 == self.depth:
                    self.curr += self.behavior('Fill')
                    self.exit_boat()
                else:
                    self.curr += self.behavior('Fill')
            else:
                if self.curr != self.depth:
                    self.curr += self.behavior('Fill')
        else:
            if self.curr > 0:
                drain = self.behavior('Drain')
                while self.curr - drain < 0:
                    drain -= 1
                self.curr -= drain

    def can_accept(self):
        return True if self.curr == 0 and self.boat_num == 0 else False
