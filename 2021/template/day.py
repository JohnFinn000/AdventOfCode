import unittest
import re
from collections import defaultdict
from collections import Counter
from numpy import sign

def calc(data):
    pass

def calc2(data):
    pass

class TestDay(unittest.TestCase):
    def test_first_sample_data(self):
        self.assertEqual(calc(open('sample').readlines()), 0)

    #def test_first_final_data(self):
    #    self.assertEqual(calc(open('data').readlines()), 0)

    #def test_second_challenge_sample(self):
    #    self.assertEqual(calc2(open('sample').readlines()), 0)

    #def test_second_final_data_2(self):
    #    self.assertEqual(calc2(open('data').readlines()), 0)

if __name__ == '__main__':
    unittest.main()
