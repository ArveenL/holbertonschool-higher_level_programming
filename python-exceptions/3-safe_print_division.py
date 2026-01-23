#!/usr/bin/python3

def safe_print_division(a, b):

    Result = None

    try:
        result = a/b
        return result
    
    except (ZeroDivisionError, TypeError):
        return None  # similar to return 0 if error found
    
    finally:
        print("Inside result: {}".format(result))
