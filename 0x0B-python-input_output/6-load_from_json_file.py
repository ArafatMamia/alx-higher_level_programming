#!/usr/bin/python3
"""
This module contain load_from_json function
"""
import json

def load_from_json_file(filename):
    """ creates an object from a 'JSON file' """
    return json.load(filename)
