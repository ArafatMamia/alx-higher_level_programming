#!/usr/bin/python3
"""
contains test for base class
"""

import unittest
from models import base
Base = base.Base

class TestBaseDocs(unittest.TestCase):
    """ Tests to check functionality of Base class """

    def test_module_docstring(self):
        """ Tests for the module docstring """
        self.assertTrue(len(base.__doc__) >= 1)
    
    def test_class_docstring(self):
        """ Tests for the Base class docstring """
        self.assertTrue(len(Base.__doc__) >= 1)
    
class TestBase(unittest.TestCase):
    """ Tests to check funcionality of Base class """

    def test_no_id(self):
        """ Tests is as None """
        b1 = Base()
        self.assertTrue(b1.id, 1)

    def test_id_set(self):
        """ test id as not None """
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_no_id_after_set(self):
        """ Tests id as None after not None """
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_nb_private(self):
        """ Tests nb_object as a private instance attribute """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)






