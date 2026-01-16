#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    #not counting program's name, 
    #counting only arguments
    args = sys.argv[1:]

    #goes one by one through list of,
    #arguments and returns its count
    args_count = len(args)

    if (args_count == 0):
        print("no arguments.")
    elif (args_count == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(args_count))

    for i in range(args_count):
        print(str[i + 1] + ": " + args[i])
        

    