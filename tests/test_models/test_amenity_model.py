#!/usr/bin/python3

import unittest
import os

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class in the models module.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment and create an instance of Amenity for testing.

        """
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Swimming Pool"

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test environment after all test methods have been run.

        """
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass



    def test_is_subclass(self):
        """
        Test if Amenity is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """
        Test the existance of a docstring for the Amenity class.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """
        Test if the Amenity instance has the expected attributes.
        """
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        """
        Test if the name attribute is a string.
        """
        self.assertEqual(type(self.amenity1.name), str)

    def test_save(self):
        """
        Test the save method of the Amenity class.
        """
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """
        Test the existance of the 'to_dict' method in the Amenity class.
        """
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
