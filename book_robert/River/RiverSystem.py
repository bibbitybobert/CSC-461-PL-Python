from book_robert.River import RiverSections as rs
from book_robert.Iterator import Iterator as i


class RiverSystem:
    boat_id = 0

    def __init__(self):
        lock = rs.Lock(0)
        lock.set_behavior(1)
        self.__it_type = 1
        self.river = []
        self.add_section(6, 0)
        self.add_lock(1, 0)
        self.add_section(3, 1)

    def __iter__(self):
        if self.__it_type == 1:
            self.__it = i.Iterator(self.river)
        else:
            self.__it = i.Iterator(self.river).get_sec_iterator()
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

    def print_sec_deets(self):
        count = 1
        self.__it_type = 2
        for sec in self:
            print('Section ' + str(count))
            sec.print_deets()
            count += 1
        self.__it_type = 1

    def new_test_river(self):
        self.clear_river()
        self.add_section(5, 0)
        self.add_lock(1, 0)
        self.add_section(6, 2)
        self.add_lock(2, 2)
        self.add_section(3, 3)
        self.add_lock(3, 5)

    def add_section(self, size, flow):
        self.river.append(rs.Section(size, flow))

    def add_lock(self, behavior, depth):
        add_lock = rs.Lock(depth)
        add_lock.set_behavior(behavior)
        self.river.append(add_lock)

    def clear_river(self):
        self.river = []
