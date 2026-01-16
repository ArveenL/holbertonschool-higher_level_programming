#!/usr/bin/python3
import sys

if __name__ == "__main__":

    #not counting program's name, 
    #counting only arguments
    args = sys.argv[1:]

    #goes through lenght of,
    #arguments to count its amount
    args_count = len(args)

    if (args_count == 0):
        print("no arguments.")
    elif (args_count == 1):
        print("1 argument:")
    else:
        print("{}: {}".format(str(args), args_count, ))