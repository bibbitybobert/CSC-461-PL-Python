from book_robert.River import RiverSections as rs


class Iterator:
    def __init__(self, in_list: list):
        self.__list = in_list
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        try:
            self.__index -= 1
            return self.__list[self.__index]

        except:
            raise StopIteration()

    def start(self):
        return self.__list[0]

    def __back__(self):
        return self.__list[-1]

    def __len__(self):
        return len(self.__list)

    def peek(self):
        try:
            return self.__list[self.__index - 1]
        except:
            return None

    def get_sec_iterator(self):
        return self.SectionIterator(self.__list)


    class SectionIterator:
        def __init__(self, in_list: list):
            self.__list = in_list
            self.__index = 0

        def __iter__(self):
            self.__index = 0
            return self

        def __next__(self):
            try:
                self.__index += 1
                while type(self.__list[self.__index]) is rs.Lock:
                    self.__index += 1
                return self.__list[self.__index]
            except:
                raise StopIteration()
