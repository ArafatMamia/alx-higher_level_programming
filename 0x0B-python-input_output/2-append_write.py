#!/usr/bin/python3

"""  
This module contain append_write function 
"""


def append_write(filename="", text=""):
    """ This function append a text """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
