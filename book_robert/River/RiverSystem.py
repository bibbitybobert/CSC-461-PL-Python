from book_robert.River import RiverSections as rs
from book_robert.Iterator import Iterator as i
from book_robert.Boat import Boat as b


class RiverSystem:
    """
    Largest manager class to take care of all operations given by the user and call appropriate sub-functions
    """

    def __init__(self):
        """
        Initialize function for RiverSystem class. Sets default values and makes default list of sections
        """
        lock = rs.Lock(0)
        lock.set_behavior(1)
        self.__it_type = 1
        self.river = []
        self.add_section(6, 0)
        self.add_lock(1, 0)
        self.add_section(3, 1)

    def __iter__(self):
        """
        Get iterator for the RiverSystem list depending on if we want it to iterate forward or backwards
        :return: iterator for the RiverSystem List
        """
        if self.__it_type == 1:
            self.__it = i.Iterator(self.river)
        else:
            self.__it = i.Iterator(self.river).get_sec_iterator()
        return self.__it

    def __str__(self):
        """
        Override the string function for RiverSystem. Will return one string split in the middle with a \n so that
        when printed out, there will be two lines for the RiverSystem. Uses an iterator to fill out the string that is
        returned
        :return: String of the RiverSystem list.
        """
        top_str = ''
        bot_str = ''
        for rsstr in self:  # GRADING: LOOP_ALL
            top_str = str(rsstr) + top_str
        top_str += '\n'
        for rsstr in self:
            bot_str = rsstr.str2() + bot_str
        return top_str + bot_str

    def add_new_boat(self, power: int, behavior: int):
        """
        Adds a new boat to the RiverSystem given an engine power for the boat and a behavior
        :param power: engine power of the boat
        :param behavior: behavior of the boat
        :return: Nothing
        """
        self.river[0].add_boat(power, behavior)

    def update(self):
        """
        Updates the entire river system by iterating through and individually updating each section
        :return: Nothing
        """
        return_boat = True
        for u in self:
            u.update(return_boat)
            can_accept = u.can_accept()
            next_section = self.__it.peek()
            if next_section is not None and can_accept:
                mov_boat = next_section.returns_boat()
                if mov_boat is not None:
                    u.import_boat(mov_boat)
            return_boat = can_accept

    def print_sec_deets(self):
        """
        Prints the details for all the 'Section' sections of the RiverSystem list. uses a restricted iterator to only
        look at the 'Section' type sections
        :return: Nothing
        """
        count = 1
        self.__it_type = 2
        for sec in self:  # GRADING: LOOP_RESTRICT
            print('Section ' + str(count))
            print(sec.print_deets())
            count += 1
        self.__it_type = 1

    def new_test_river(self):
        """
        Adds a new test river with 6 sections (3 'Sections', 3 'Locks')
        :return: Nothing
        """
        self.clear_river()
        self.add_section(5, 0)
        self.add_lock(1, 0)
        self.add_section(6, 2)
        self.add_lock(2, 2)
        self.add_section(3, 3)
        self.add_lock(3, 5)

    def add_section(self, size, flow):
        """
        Adds a 'Section' Type section to the RiverSystem list
        :param size: number of subsections in this section type
        :param flow: flow of the river in this area
        :return: Nothing
        """
        self.river.append(rs.Section(size, flow))

    def add_lock(self, behavior, depth):
        """
        Adds a 'Lock' Type section to the RiverSystem list
        :param behavior: behavior of the lock
        :param depth: depth of the lock
        :return: Nothing
        """
        add_lock = rs.Lock(depth)
        add_lock.set_behavior(behavior)
        self.river.append(add_lock)

    def clear_river(self):
        """
        Clears the RiverSystem list to make it ready to take in new custom sections
        :return: Nothing
        """
        self.river = []

    def print_boat_forms(self):
        """
        Function that adds three new boats, only puts one in the river, and shows what each class will print out
        (secret extra instruction in main menu: -1)
        :return: nothing
        """
        new_boat_1 = b.Boat(1)
        new_boat_2 = b.Boat(1)

        subsec = rs.SubSec(-1)
        subsec.add_boat(new_boat_1)

        test_lock = rs.Lock(0)
        test_lock.import_boat(new_boat_2)

        self.add_new_boat(1, 1)

        # GRADING: TO_STR
        print(new_boat_1)
        print(subsec)
        print(test_lock)
        print(self)
