from book_robert.River import RiverSystem

'''
Grading tags in for all lines marked with *			_yes_

Tierless str meets D in SOLID (hidden test)*			_Yes_
Check if above is done, but not its test was not reached	___

1. Initial Show system\Got it compiling
Menu\initial system working					_yes_
Bad input handled						_yes_

2. Add Default
Added and shown properly					_yes_
Second+ item ignored						_yes_

3. Basic Update (single)
Moves along section						_yes_
String format correct						_yes_
Iterator used*							_yes_

4. Basic Update (multiple)					_yes_

5. Multi Update
Updates correctly						_yes_
Bad input handled						_yes_

6. Show details
Shows details properly 						_yes_
Iterator used*							_yes_

6. Add user specified item
Basic movement still works					_yes_
Powered works							_yes_
No passing							_yes_

7. Tester part 1
Boats works up to second lock 					_yes_
Formatting correct 						_yes_

8. Tester part 2
Boats works up to end						_yes_
Strategy pattern for basic fill*				_yes_
Strategy pattern for fast empty*				_yes_

9. Custom belt **
String formatting correct					_yes_
Everything still works 						_yes_
Bad input handled 						_yes_
'''


def cleanInput(prompt):
    result = input(prompt)
    # strips out blank lines in input
    while result == '':
        result = input()

    return result

def main():
    river = RiverSystem.RiverSystem()
    menu = "\n" \
           "1) Add Default Boat\n" \
           "2) Update One Tick\n" \
           "3) Update X Ticks\n" \
           "4) Show Section Details\n" \
           "5) Add Boat\n" \
           "6) Make Tester\n" \
           "7) Make New Simulator\n" \
           "0) Quit\n"

    choice = -1
    print(str(river))
    while choice != 0:
        print(menu)
        try:
            choice = cleanInput("Choice:> ")
            if choice.isnumeric() or choice == '-1':
                choice = int(choice)
            elif choice.isalpha():
                raise TypeError

            match choice:
                case 1:  # add default boat
                    river.add_new_boat(1, 1)
                    print(river)
                case 2:  # update one tick
                    river.update()
                    print(river)
                case 3:  # update X ticks
                    update_num = cleanInput('How many updates:> ')
                    if update_num.isalpha():
                        raise TypeError
                    elif update_num.isnumeric():
                        update_num = int(update_num)

                    for i in range(0, update_num):
                        river.update()
                        if i != update_num -1:
                            print(str(river) + '\n')
                    print(river)
                case 4:  # print out section details
                    river.print_sec_deets()
                case 5:  # add a new boat
                    eng_pow = cleanInput('What engine power:> ')
                    if not eng_pow.isdigit():
                        raise TypeError
                    else:
                        eng_pow = int(eng_pow)
                        if eng_pow < 0:
                            raise TypeError
                    trav_met = cleanInput('What travel method. (1) Steady or (2) Max :> ')
                    if trav_met.isalpha():
                        raise TypeError
                    else:
                        trav_met = int(trav_met)
                    if trav_met < 1 or trav_met > 2:
                        raise ValueError
                    else:
                        river.add_new_boat(eng_pow, trav_met)

                    print(river)
                case 6:  # make new tester
                    river.new_test_river()
                    print(river)
                case 7:  # make new sim
                    sim_choice = 'y'
                    new_river = RiverSystem.RiverSystem()
                    new_river.clear_river()
                    while sim_choice != 'n':
                        try:
                            s_or_l = cleanInput('Section (1) or Lock (2):> ')
                            if s_or_l.isalpha():
                                raise ArithmeticError
                            s_or_l = int(s_or_l)
                            if s_or_l == 1:
                                new_len = cleanInput('Length:> ')
                                if new_len.isalpha():
                                    raise ArithmeticError
                                new_len = int(new_len)
                                new_flow = cleanInput('Flow:> ')
                                if new_flow.isalpha():
                                    raise ArithmeticError
                                new_flow = int(new_flow)
                                new_river.add_section(new_len, new_flow)
                            elif s_or_l == 2:
                                new_behavior = cleanInput('Fill behavior: None (1), Basic (2), or Fast Empty (3):> ')
                                if new_behavior.isalpha():
                                    raise ArithmeticError
                                new_behavior = int(new_behavior)
                                if new_behavior < 1 or new_behavior > 3:
                                    raise ArithmeticError
                                new_depth = cleanInput('Depth:> ')
                                if new_depth.isalpha():
                                    raise ArithmeticError
                                new_depth = int(new_depth)
                                new_river.add_lock(new_behavior, new_depth)
                            else:
                                raise ValueError
                        except TypeError:
                            print('Please, input a positive integer')
                        except ValueError:
                            print('Input an option in the range 1-2')
                        except ArithmeticError:
                            print('Cannot accept value')
                        sim_choice = cleanInput('\nAdd another component (n to stop):> ')

                    river = new_river
                    print(river)
                case 0:  # quit
                    choice = 0
                case -1:  # error
                    river.print_boat_forms()
                case _:  # default
                    print('Input an option in the range 0-7')

        except TypeError:
            print('Please, input a positive integer')
        except ValueError:
            print('Input an option in the range 1-2')
            print(river)
        except ArithmeticError:
            print('Cannot accept value')
        except:
            import traceback
            print(traceback.format_exc())


if __name__ == '__main__':
    main()
