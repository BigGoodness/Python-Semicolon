from unittest import TestCase
#import unittest 
#import arithmetic_operation
from arithmetic_operation import *
 
class TestCase(TestCase):

    def sum_of_two_numbers(self):

        expected = sum_of_two_numbers(7, 9)
        actual = 16
        self.assertEqual(expected, actual)
