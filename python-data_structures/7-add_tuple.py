#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Get first element of tuple_a, or 0 if it doesn't exist
    # Why: Tuples might have 0 or 1 element
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0

    # Get second element of tuple_a, or 0 if it doesn't exist
    # Why: We only care about the first two elements
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # Get first element of tuple_b, or 0 if it doesn't exist
    # Why: Same logic as above
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0

    # Get the second element of tuple_b, or 0 if it doesn't exist
    # Why: Same logic as above
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
