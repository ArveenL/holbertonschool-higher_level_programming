#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for item in row:
            # Format each integer to take at least 4 spaces for alignment
            print(f"{item:4}", end=" ")
        print()  # Print a new line after each row
