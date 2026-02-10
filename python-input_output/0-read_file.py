#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as justavariable:  # opens file and auto-close it
        print(justavariable.read(), end="")
