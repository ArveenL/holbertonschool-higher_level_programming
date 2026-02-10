#!/usr/bin/env python3
"""
Docstring for python-abc.task_03_countediterator
"""



class CountedIterator:
    def __init__(self, iterable):
        self._iter = iter(iterable)  # store the iterator
        self.count = 0               # initialize counter

    def get_count(self):
        return self.count            # return current count

    def __next__(self):
        try:
            item = next(self._iter)  # get next item
            self.count += 1           # increment counter
            return item
        except StopIteration:
            raise                   # propagate StopIteration if done
