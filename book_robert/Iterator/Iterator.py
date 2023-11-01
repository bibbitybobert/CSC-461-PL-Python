from book_robert.River import RiverSections as rs


class Iterator:
    """
    Basic backwards iterator. Used in RiverSystem and Section river part
    """
    def __init__(self, in_list: list):
        """
        Initializes new Iterator when new obj created
        :param in_list: the list that user wants to iterate through
        """
        self.__list = in_list
        self.__index = 0

    def __iter__(self):  # GRADING: ITER_ALL
        """
        used in for-each loop to create iterator that will set index to 0 and return iterator that increments through
         list
        :return: the Iterator
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        used to get the next obj in the list (at index -1)
        :return: the next obj in the list
        """
        try:
            self.__index -= 1
            return self.__list[self.__index]

        except:
            raise StopIteration()

    def start(self):
        """
        gets the first value in the list (last iterated through)
        :return: first value in the list
        """
        return self.__list[0]

    def __back__(self):
        """
        gets the last value in the list (first iterated through)
        :return: obj at the back of the list
        """
        return self.__list[-1]

    def __len__(self):
        """
        gets the length of the list that is being iterated through
        :return:  length of the list
        """
        return len(self.__list)

    def peek(self):
        """
        peek at next value in the iteration without moving the index pointer
        :return: next obj in the iteration
        """
        try:
            return self.__list[self.__index - 1]
        except:
            return None

    def get_sec_iterator(self):
        """
        get an iterator that only returns the 'Section' river part
        :return: a restricted iterator
        """
        return Iterator.SectionIterator(self.__list)

    class SectionIterator:  # GRADING: ITER_RESTRICT
        """
        A forward iterator that will only iterate through the 'Section' type river part
        """
        def __init__(self, in_list: list):
            """
            initializes the iterator
            :param in_list: list to iterate through
            """
            self.__list = in_list
            self.__index = -1

        def __iter__(self):
            """
            Iterator pointer. Used by for-each loop to start iteration at the beginning
            :return: the iterator
            """
            self.__index = -1
            return self

        def __next__(self):
            """
            get the next 'Section' river part in the given list
            :return: the next 'Section' river part
            """
            try:
                self.__index += 1
                while type(self.__list[self.__index]) is not rs.Section:
                    self.__index += 1
                return self.__list[self.__index]
            except:
                raise StopIteration()
