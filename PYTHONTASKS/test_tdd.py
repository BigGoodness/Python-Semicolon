from unittest import TestCase

from integer_number import *

 
class TestCase(TestCase):

    def test_that_division_of_two_numbers(self):
        expected = division_of_two_numbers(25, 5)
        actual = 3
        self.assertEqual(expected, actual)


#    def test_that_first_number_is_negative(self):
#        expected = first_number_is_negative(-25, 5)
#        actual = 
#        self.assertEqual(expected, actual)
