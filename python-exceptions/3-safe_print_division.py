#!/usr/bin/python3

def safe_print_division(a, b):

    result = None

    try:
        result = a / b       # assign result first

    except (ZeroDivisionError, TypeError):
        result = None        # assign None if division fails

    finally:
        print("Inside result: {}".format(result))

    return result             # return result after finally
