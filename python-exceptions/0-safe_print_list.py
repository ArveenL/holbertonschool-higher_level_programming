#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break

    print()
    return count

    # _Notes_ ################################
    # 1. count = tracks actual amount of x-element
    #    +1 every time we have printed one element
    #
    # 1.5 note: printing my_list[i] prints element
    #     per element, not the whole list at once
    #
    # 2. except IndexError is like saying "until NULL"
    #    in C language
    #
    # 3. second print() is to print a new line
    #    as required by the question
    #
    # 4. return count to confirm actual amount
    #    of x elements printed
    #
    # 5. indent second print() and return count
    #    at the same level as the for loop
