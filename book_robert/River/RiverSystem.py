import RiverSections as rs
class RiverSystem:
    boat_id = 0
    def __init__(self):
        self.__river = [rs.Section(0), rs.Section(0), rs.Section(0), rs.Section(0), rs.Section(0), rs.Section(0),
                        rs.Lock(0, 0), rs.Section(0), rs.Section(0), rs.Section(0)]

    def __iter__(self):
        self.__index = -1
        return self

    def __str__(self):
        top_str = ''
        bot_str = ''
        for i in self.__river:
            top_str += i.top_char
            bot_str += i.bot_char

        return top_str + '\n' + bot_str

    def __next__(self):
        try:
            self.__index += 1
            return self.__river[self.__index]
        except:
            raise StopIteration()

    def add_new_boat(self):
        self.boat_id += 1
        if not self.__river[0].has_boat:
            self.__river[0].add_boat(self.boat_id)

