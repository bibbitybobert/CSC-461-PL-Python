from book_robert.Boat import Boat as b
from book_robert.Iterator import Iterator as it
from book_robert.Boat import BoatBehavior as bb
from book_robert.River import LockBehavior as lb


class RiverPart:
    """
    Parent class for both other Sections used in the RiverSystem list
    """
    def __init__(self):
        """
        Initializes this class with a count of boats in this section at 0
        """
        self.boat_num = 0


class Section(RiverPart):
    """
    Child class of RiverPart that is an area of open water for a boat to move through
    """
    def __init__(self, size: int, flow: int):
        """
        Initializes this class with a flow, size and list of subsections to track where a boat is
        :param size: number of subsections in list
        :param flow: flow of the river (used in update to determine where boats move)
        """
        super().__init__()
        self.flow = flow
        self.subsec = []
        self.size = size
        for i in range(0, size):
            self.subsec.append(SubSec(i))

    def __iter__(self):
        """
        Creates an iterator to increment through the list easily
        :return: an iterator for the Section list
        """
        return it.Iterator(self.subsec)

    def __str__(self):
        """
        overridden str function for 'Section' type. Will return a string of all the chars in the list
        :return: string of all the string values in the list
        """
        out_str = ''
        for sstr in self:
            out_str = str(sstr) + out_str
        return out_str

    def str2(self):
        """
        secondary string function to return the lower part of each subsection
        :return: string of the lower part of this section
        """
        out_str = ''
        for bstr in self:
            out_str = bstr.str2() + out_str
        return out_str

    def add_boat(self, power: int, method: int):
        """
        adds a boat to the beginning of this section with a given power and movement method
        :param power: engine power of the boat
        :param method: movement method of the boat
        :return: Nothing
        """
        new_boat = b.Boat(power)
        if not self.subsec[0].has_boat:
            new_boat.setBehavior(method)
            new_boat.speed = new_boat.behavior(power, self.flow)
            self.subsec[0].add_boat(new_boat)
            self.boat_num += 1

    def returns_boat(self):
        """
        Determines if the section will have a boat leave it in the next update
        :return: Boat that will leave the section in the next update or None if there is no boat leaving
        """
        if self.subsec[-1].has_boat:
            self.boat_num -= 1
            return self.subsec[-1].boat
        return None

    def update(self, return_boat):
        """
        Updates the section, moves boat an appropriate distance determined by their behavior and availability in the
        list and availability of next section
        :param return_boat: boolean value if a boat can move into the next section
        :return:
        """
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
        """
        Prints details of this section (num of boats, flow value)
        :return: string with details of this section
        """
        return 'Boats: ' + str(self.boat_num) + ' Flow: ' + str(self.flow) + '\n'

    def can_accept(self):
        """
        determines if this section can accept a boat
        :return: True if there is availability, false if not
        """
        if not self.subsec[0].has_boat:
            return True
        return False

    def import_boat(self, boat: b.Boat):
        """
        Adds a preexisting boat to the section (instead of making a new one like in add_boat())
        :param boat: preexisting boat to add to section
        :return: Nothing
        """
        self.subsec[0].add_boat(boat)
        self.subsec[0].boat.speed = boat.behavior(boat.power, self.flow)
        self.boat_num += 1


class SubSec:
    """
    Subsection of the 'Section' Class
    """
    def __init__(self, loc):
        """
        Initializes the subsection with strings and default parameters. Takes in one value: location, to be used later
        with calculating where a boat will move when updating the system
        :param loc: location of the subsection
        """
        self.char = '〜〜〜'
        self.bot = '〜〜〜'
        self.has_boat = False
        self.boat = None
        self.addr = loc

    def add_boat(self, boat: b.Boat):
        """
        Add a boat to the subsection
        :param boat: boat to add to the subsection
        :return:  Nothing
        """
        self.has_boat = True
        self.boat = boat
        self.char = str(boat).ljust(3, '〜')
        self.bot = str(boat.id).ljust(3, '〜')

    def remove_boat(self):
        """
        Remove a boat from the subsection
        :return: Nothing
        """
        self.has_boat = False
        self.boat = None
        self.char = '〜〜〜'
        self.bot = '〜〜〜'

    def __str__(self):
        """
        Override string function for this class
        :return: a string that represents this subsection in its current state
        """
        return self.char

    def str2(self):
        """
        secondary string function to return the lower string of this class
        :return: string of the lower area of this class
        """
        return self.bot

    def returns_boat(self):
        """
        function to determine if this subsection will return a boat at the next update
        :return: the boat that will be returned next section, or None if no boat will be returned
        """
        if self.has_boat:
            return self.boat
        else:
            return None


class Lock(RiverPart):
    """
    Lock section in the RiverSystem list
    """
    def __init__(self, depth: int):
        """
        Initializes this class with default parameters whenever a new instance is created
        :param depth: depth of the Lock
        """
        super().__init__()
        self.depth = depth
        self.curr = 0
        self.top_char = '_X(' + str(self.curr).rjust(2) + ')_'
        self.bot_char = '.' * 7
        self.behavior = None
        self.boat = None

    def import_boat(self, boat: b.Boat):
        """
        Import a preexisting boat
        :param boat: preexisting boat to import
        :return: Nothing
        """
        self.boat = boat
        self.boat_num = 1
        self.top_char = '_' + str(self.boat) + '(' + str(self.curr).rjust(2) + ')_'
        self.bot_char = str(boat.id).ljust(2, '.') + self.bot_char[2:]

    def set_behavior(self, behavior: int):
        """
        set the behavior of this lock depending on an instruction by the user
        :param behavior: an integer to determine what behavior the user wants this lock to have
        :return: Nothing
        """
        if behavior == 1:
            self.behavior = lb.pass_through
        elif behavior == 2:
            self.behavior = lb.basic
        else:
            self.behavior = lb.fast

    def __str__(self):
        """
        Overridden string function to print this section out to the console
        :return: a string to represent this class
        """
        self.top_char = self.top_char[0:3] + str(self.curr).rjust(2) + self.top_char[5:]
        return self.top_char

    def str2(self):
        """
        Secondary string function to get the lower string part of the Lock
        :return: string with the lower chars of the Lock
        """
        return self.bot_char

    def returns_boat(self):
        """
        Checks if the function returns a boat at the next update
        :return: The boat that will return or None if no boat
        """
        if self.boat_num == 1 and self.curr + 1 >= self.depth:
            return self.boat
        else:
            return None

    def exit_boat(self):
        """
        Remove a boat from the Lock
        :return: Nothing
        """
        self.boat = None
        self.boat_num = 0
        self.top_char = '_X(' + str(self.curr).rjust(2) + ')_'
        self.bot_char = '..' + self.bot_char[2:]

    def update(self, return_boat):
        """
        Update the lock
        :param return_boat: Boolean if the lock can return a boat to the next section
        :return: Nothing
        """
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
        """
        determines if the Lock can accept an incoming boat
        :return: True if Lock can accept a boat, false if not
        """
        return True if self.curr == 0 and self.boat_num == 0 else False
