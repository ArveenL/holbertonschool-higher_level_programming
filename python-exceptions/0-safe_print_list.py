#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    
    count = 0
    
    for i in range(x):
        try:
            print(my_list[i], end="")
            count = count + 1
        
        except IndexError:
            break
        
    print()
    return count

############_Notes_################################
    # 1. count = tracks actual amount of x-element
    #           + 1 with it every time we've 
    #           printed 1 x-element

    # 1.5. note printing my_list[i] to print element
    # per element and not the whole list at once

    # 2. except IndexError is like saying "until NULL"
    #   in C language

    # 3.  2nd print() is to print new line as per the question

    # 4. return count to confirm actual amount of x element printed

    # 5. indent 2nd print and return count same column as for loop