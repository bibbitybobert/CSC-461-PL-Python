from book_robert.River import RiverSections as rs


class RiverSystem:
    boat_id = 0

    def __init__(self):
        self.__river = [rs.Section(0), rs.Section(0), rs.Section(0), rs.Section(0), rs.Section(0), rs.Section(0),
                        rs.Lock(0, 0), rs.Section(0), rs.Section(0), rs.Section(0)]

    def __iter__(self):
        self.__index = 0
        return self

    def __str__(self):
        top_str = ''
        bot_str = ''
        for i in self:
            top_str = i.top_char + top_str
            bot_str = i.bot_char + bot_str

        return top_str + '\n' + bot_str

    def __next__(self):
        try:
            self.__index -= 1
            return self.__river[self.__index]
        except:
            raise StopIteration()

    def __peek__(self):
        try:
            return self.__river[self.__index - 1]
        except:
            return False


    def start(self):
        return self.__river[0]

    def add_new_boat(self):
        self.boat_id += 1
        if not self.start().boat:
            self.start().add_boat(self.boat_id)

    def update(self):
        for i in self:
            i.update()
            if self.__peek__() and self.__peek__().boat:
                boat_id = self.__peek__().boat.id
                power = self.__peek__().boat.power
                i.add_boat(boat_id, power)


