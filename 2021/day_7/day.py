import unittest
import re
from collections import defaultdict
from collections import Counter
from numpy import sign

def calc(data):
    p = map(int, data.split(","))
    crabs = defaultdict(int)
    low = p[0]
    high = p[0]
    for point in p:
        crabs[point] += 1
        low = min(point, low)
        high = max(point, high)
    best_cost = 999999999999999
    for i in range(low, high+1):
        cost = 0
        for k, v in crabs.iteritems():
            cost += abs(k-i)*v
        if cost < best_cost:
            best_cost = cost
    return best_cost

def calc_2(data):
    p = map(int, data.split(","))
    crabs = defaultdict(int)
    low = p[0]
    high = p[0]
    for point in p:
        crabs[point] += 1
        low = min(point, low)
        high = max(point, high)
    best_cost = 999999999999999
    for i in range(low, high+1):
        cost = 0
        for k, v in crabs.iteritems():
            d = abs(k-i)
            cost += (((d+1)*d)/2)*v 
        if cost < best_cost:
            best_cost = cost
    return best_cost

class TestDay(unittest.TestCase):
    sample = "16,1,2,0,4,2,7,1,2,14"

    def test_first_sample_data(self):
        self.assertEqual(calc(self.sample), 37)

    def test_first_final_data(self):
        self.assertEqual(calc(open('data').readlines()[0]), 349769)

    def test_second_challenge_sample(self):
        self.assertEqual(calc_2(self.sample), 168)

    def test_second_final_data_2(self):
        self.assertEqual(calc_2(open('data').readlines()[0]), 99540554)

if __name__ == '__main__':
    unittest.main()
