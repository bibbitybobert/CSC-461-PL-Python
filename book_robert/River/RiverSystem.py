from book_robert.River import RiverSections as rs
from book_robert.Iterator import Iterator as i


class RiverSystem:
    boat_id = 0

    def __init__(self):
        lock = rs.Lock(0, 0)
        lock.set_behavior(1)
        self.river = list([rs.Section(6, 0), lock, rs.Section(3, 0)])

    def __iter__(self):
        self.__it = i.Iterator(self.river)
        return self.__it

    def __str__(self):
        top_str = ''
        bot_str = ''
        for rsstr in self:
            top_str = str(rsstr) + top_str
        top_str += '\n'
        for rsstr in self:
            bot_str = rsstr.str2() + bot_str
        return top_str + bot_str

    def add_new_boat(self, power: int, behavior: int):
        self.boat_id += 1
        self.river[0].add_boat(self.boat_id, power, behavior)

    def update(self):
        for u in self:
            u.update()
            can_accept = u.can_accept()
            next_section = self.__it.peek()
            if next_section is not None:
                mov_boat = next_section.returns_boat()
                if mov_boat is not None and can_accept:
                    u.import_boat(mov_boat)
