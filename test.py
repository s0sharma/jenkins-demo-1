#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from utils import add

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = [23, 32]
        result = add(data[0], data[1])
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()
