import unittest

from main import p1, p2
from utils import read_strings_list, read_sections, parse_pairs, parse_ints


class Test(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test, if needed
        self.example_file = 'example.txt'
        self.input_file = 'input.txt'

    def test_p1_example(self):
        part1, part2 = read_sections(self.example_file)
        page_ordering_rules = parse_pairs(part1)
        pages_to_produce = parse_ints(part2)
        result = p1(page_ordering_rules, pages_to_produce)
        self.assertEqual(143, result)

    def test_p1_input(self):
        part1, part2 = read_sections(self.input_file)
        page_ordering_rules = parse_pairs(part1)
        pages_to_produce = parse_ints(part2)
        result = p1(page_ordering_rules, pages_to_produce)
        self.assertEqual(4462, result)

    def test_p2_example(self):
        part1, part2 = read_sections(self.example_file)
        page_ordering_rules = parse_pairs(part1)
        pages_to_produce = parse_ints(part2)
        result = p2(page_ordering_rules, pages_to_produce)
        self.assertEqual(123, result)

    def test_p2_input(self):
        part1, part2 = read_sections(self.input_file)
        page_ordering_rules = parse_pairs(part1)
        pages_to_produce = parse_ints(part2)
        result = p2(page_ordering_rules, pages_to_produce)
        self.assertEqual(6767, result)

    def tearDown(self):
        # Cleanup code to run after each test, if needed
        pass


if __name__ == '__main__':
    unittest.main()
