#!/usr/bin/python3
def fizzbuzz():
    for c in range(1,101):
    
        if (c % 15 == 0):
            print("fizzbuzz", end=" ")
        elif (c % 3 == 0):
            print("fizz", end=" ")
        elif (c % 5 == 0):
            print("buzz", end=" ")
        else:
            print(c, end=" ")
