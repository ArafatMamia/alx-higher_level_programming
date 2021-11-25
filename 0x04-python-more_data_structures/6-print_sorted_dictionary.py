#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if(a_dictionary):
        for val1, val2 in sorted(a_dictionary.items()):
            print("{}: {}".format(val1, val2))
