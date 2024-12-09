import unittest

from main import p1, p2
from utils import read_strings_list


class Test(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test, if needed
        self.example_file = 'example.txt'
        self.input_file = 'input.txt'

    def test_p1_example(self):
        strings_list = read_strings_list(self.example_file)
        result = p1(strings_list)
        self.assertEqual(3749, result)

    def test_p1_input(self):
        strings_list = read_strings_list(self.input_file)
        result = p1(strings_list)
        self.assertEqual(3312271365652, result)

    def test_p2_example(self):
        strings_list = read_strings_list(self.example_file)
        result = p2(strings_list)
        self.assertEqual(11387, result)

    def test_p2_input(self):
        strings_list = read_strings_list(self.input_file)
        result = p2(strings_list)
        self.assertEqual(509463489296712, result)


    def tearDown(self):
        # Cleanup code to run after each test, if needed
        pass

if __name__ == '__main__':
    unittest.main()
