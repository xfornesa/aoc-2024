import unittest

from main import p1, p2
from utils import read_pair_of_int_lists


class Test(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test, if needed
        self.example_file = 'example.txt'
        self.input_file = 'input.txt'

    def test_p1_example(self):
        # Test read_pairs function with input file
        # Add expected pairs for input file if known
        pair_of_lists = read_pair_of_int_lists(self.example_file)
        result = p1(pair_of_lists)
        self.assertEqual(result, 11)

    def test_p1_input(self):
        # Test read_pairs function with input file
        # Add expected pairs for input file if known
        pair_of_lists = read_pair_of_int_lists(self.input_file)
        result = p1(pair_of_lists)
        self.assertEqual(result, 1879048)

    def test_p2_example(self):
        # Test read_pairs function with input file
        # Add expected pairs for input file if known
        pair_of_lists = read_pair_of_int_lists(self.example_file)
        result = p2(pair_of_lists)
        self.assertEqual(result, 31)

    def test_p2_input(self):
        # Test read_pairs function with input file
        # Add expected pairs for input file if known
        pair_of_lists = read_pair_of_int_lists(self.input_file)
        result = p2(pair_of_lists)
        self.assertEqual(result, 21024792)

    def tearDown(self):
        # Cleanup code to run after each test, if needed
        pass

if __name__ == '__main__':
    unittest.main()
