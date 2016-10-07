# Unit test for class Crawler2
from Crawler2 import get_inverted_index, get_resolved_inverted_index, print_inverted_index, print_resolved_inverted_index
import unittest

class TestCrawler2(unittest.TestCase):

	# the two test outputs given in the handout
    def test_print_inverted_index(self):
        self.assertEqual(print_inverted_index(), "{ '1': set([1]), '2': set([1, 2, 3]), '3': set([1]), '4': set([1, 3]), '5': set([1, 3]), '6': set([1, 3]) }, '7': set([2]) }, '8': set([2]) }, '9': set([2]) }")

    def test_print_resolved_inverted_index(self):
        self.assertEqual(print_resolved_inverted_index(), "{ 'words': set(['Yahoo']), 'search': set(['Yahoo', 'google', 'bing'])}")

if __name__ == '__main__':
    unittest.main()
