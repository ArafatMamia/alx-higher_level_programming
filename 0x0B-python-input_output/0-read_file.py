#!/usr/bin/python3
""" contains ther read_file function """

def read_file(filename=""):
    """ the read_file function that read a text file and prints it """ 
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read())
