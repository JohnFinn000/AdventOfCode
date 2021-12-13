import unittest
import re
from collections import defaultdict
from numpy import sign

def calc(data):
  d = defaultdict(int)
  for l in data:
    x1, y1, x2, y2 = map(int, re.match("(\d+),(\d+) -> (\d+),(\d+)", l).groups())
    if x1 == x2:
      if y1 > y2:
        y1, y2 = y2, y1
      for i in range(y1,y2+1):
        d[x1,i] += 1
    if y1 == y2:
      if x1 > x2:
        x1, x2 = x2, x1
      for i in range(x1,x2+1):
        d[i, y1] += 1

  return sum([1 for k, v in d.iteritems() if v > 1])

def iterate(line):
  x1, y1, x2, y2 = line
  x = x2 - x1
  y = y2 - y1
  d = max(abs(x), abs(y))
  x = sign(x)
  y = sign(y)
  for i in range(d+1):
    yield x1+x*i, y1+y*i

def calc_2(data):
  d = defaultdict(int)
  for l in data:
    for x, y in iterate(map(int, re.match("(\d+),(\d+) -> (\d+),(\d+)", l).groups())):
      d[x, y] += 1

  print [k for k, v in d.iteritems() if v > 1]
  return sum([1 for k, v in d.iteritems() if v > 1])

class TestDay(unittest.TestCase):
    sample = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2",
]

    def test_first_challenge_data(self):
        self.assertEqual(calc(self.sample), 5)

    def test_final_data(self):
        self.assertEqual(calc(open('data').readlines()), 7436)

    def test_second_challenge_sample(self):
        self.assertEqual(calc_2(self.sample), 12)

    def test_final_data_2(self):
        self.assertEqual(calc_2(open('data').readlines()), 21104)

if __name__ == '__main__':
    unittest.main()
