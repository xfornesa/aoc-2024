import unittest

from main import p1, p2
from utils import read_array_of_ints


class Test(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test, if needed
        self.example_file = 'example.txt'
        self.input_file = 'input.txt'

    def test_p1_example(self):
        array_of_ints = read_array_of_ints(self.example_file)
        result = p1(array_of_ints)
        self.assertEqual(result, 2)

    def test_p1_input(self):
        array_of_ints = read_array_of_ints(self.input_file)
        result = p1(array_of_ints)
        self.assertEqual(result, 502)

    def test_p2_example(self):
        array_of_ints = read_array_of_ints(self.example_file)
        result = p2(array_of_ints)
        self.assertEqual(result, 4)

    def test_p2_input(self):
        array_of_ints = read_array_of_ints(self.input_file)
        result = p2(array_of_ints)
        self.assertEqual(result, 544)


    def tearDown(self):
        # Cleanup code to run after each test, if needed
        pass

if __name__ == '__main__':
    unittest.main()
