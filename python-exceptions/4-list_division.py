#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element two lists up to list_length.
    Returns a new list with results or 0 if division fails.
    Prints messages for errors: wrong type, division by 0, out of range.
    """

    result = []  # new list to store division results

    for i in range(list_length):  # iterate over indexes
        try:
            # attempt to divide element i of both lists
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")  # element in list2 is zero
            division = 0
        except (TypeError, ValueError):
            print("wrong type")  # element not int/float
            division = 0
        except IndexError:
            print("out of range")  # list too short
            division = 0
        finally:
            result.append(division)  # always add a value to result

    return result
