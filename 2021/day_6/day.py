import unittest
import re
from collections import defaultdict
from collections import Counter
from numpy import sign

def iterate(f):
  n = defaultdict(int)
  for k, v in f.iteritems():
    k -= 1
    if k < 0:
      n[8] = v
      n[6] += v
    else:
      n[k] += v
  return n

def calc(data, days=80):
  f = Counter(map(int, data.split(",")))
  for i in range(days):
    f = iterate(f)
  return sum(f.values())
    

class TestDay(unittest.TestCase):
    sample = "3,4,3,1,2"

    def test_first_challenge_data(self):
        self.assertEqual(calc(self.sample), 5934)

    def test_final_data(self):
        self.assertEqual(calc(open('data').readlines()[0]), 391671)

    def test_second_challenge_sample(self):
        self.assertEqual(calc(self.sample, 256), 26984457539)

    def test_final_data_2(self):
        self.assertEqual(calc(open('data').readlines()[0], 256), 1754000560399)

if __name__ == '__main__':
    unittest.main()
