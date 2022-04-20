#!/usr/bin/python3
""" 
this module contain write_file function
"""


def write_file(filename="",text=""):
    """ write_file function that write a text and return a number of characters"""
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
