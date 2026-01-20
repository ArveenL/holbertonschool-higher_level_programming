#!/usr/bin/python3

def multiple_returns(sentence):

    first_char = 0

    if len(sentence) > 0:
        first_char = sentence[0]

    else:
        sentence[0] = None

    return (len(sentence), first_char)
