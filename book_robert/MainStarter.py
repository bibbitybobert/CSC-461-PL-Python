from book_robert.River import RiverSystem

'''
Grading tags in for all lines marked with *			___

Tierless str meets D in SOLID (hidden test)*			___
Check if above is done, but not its test was not reached	___

1. Initial Show system\Got it compiling
Menu\initial system working					___
Bad input handled						___

2. Add Default
Added and shown properly					___
Second+ item ignored						___

3. Basic Update (single)
Moves along section						___
String format correct						___
Iterator used*							___

4. Basic Update (multiple)					___

5. Multi Update
Updates correctly						___
Bad input handled						___

6. Show details
Shows details properly 						___
Iterator used*							___

6. Add user specified item
Basic movement still works					___
Powered works							___
No passing							___

7. Tester part 1
Boats works up to second lock 					___
Formatting correct 						___

8. Tester part 2
Boats works up to end						___
Strategy pattern for basic fill*				___
Strategy pattern for fast empty*				___

9. Custom belt **
String formatting correct					___
Everything still works 						___
Bad input handled 						___
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
    while choice != 0:
        print(str(river))
        print(menu)
        try:
            choice = int(cleanInput("Choice:> "))
        except:
            print('Please, input a positive integer.')

        match choice:
            case 1:  # add default boat
                river.add_new_boat()
            case 2:  # update one tick
                river.update()
            case 3:  # update X ticks
                try:
                    update_num = int(cleanInput('How many updates:> '))
                    for i in range(0, update_num):
                        river.update()
                        if i != update_num -1:
                            print(str(river) + '\n')
                except:
                    print('Please, input a positive integer.')
            case 4:  # print out section details
                print('TODO')
            case 5:  # add a new boat
                print('TODO')
            case 6:  # make new tester
                print('TODO')
            case 7:  # make new sim
                print('TODO')
            case 0:  # quit
                print('exiting')
            case -1:  #error
                print('TODO')
            case _:  # default
                print('Input an option in the range 0-7')




main()
