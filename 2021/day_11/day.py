import unittest
import re
from collections import defaultdict
from collections import Counter
from numpy import sign

def cleanup_data(data):
    cleaned_data = []
    for row in data:
        cleaned_data.append([int(value) for value in row.strip()])
    return cleaned_data

def step(data):
    flash = set()
    max_y = len(data)
    max_x = len(data[0])
    for y in range(0, max_y):
        for x in range(0, max_x):
            data[y][x] += 1
            if data[y][x] > 9:
                flash.add((x,y))

    flashed = set()
    while len(flash):
        f = flash.pop()
        flashed.add(f)
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0:
                    continue
                xa = f[0]+x
                ya = f[1]+y
                if xa < 0 or ya < 0:
                    continue
                if xa >= max_x or ya >= max_y:
                    continue
                data[ya][xa] += 1
                if data[ya][xa] > 9:
                    if (xa, ya) not in flashed:
                        flash.add((xa, ya))
                
    for f in flashed:
        data[f[1]][f[0]] = 0               
    return data, len(flashed)


def calc(data):
    data = cleanup_data(data)
    flashes = 0
    for s in range(0, 100):
        data, flash_count = step(data)
        #print("Step %r flashcount %r" % (s, flash_count))
        flashes += flash_count
    return flashes

def calc2(data):
    data = cleanup_data(data)
    s = 1
    while True:
        data, flash_count = step(data)
        if flash_count == 100:
            break
        s += 1
    return s


class TestDay(unittest.TestCase):
    def test_first_sample_data(self):
        self.assertEqual(calc(open('sample').readlines()), 1656)

    def test_first_final_data(self):
        self.assertEqual(calc(open('data').readlines()), 1732)

    def test_second_challenge_sample(self):
        self.assertEqual(calc2(open('sample').readlines()), 195)

    def test_second_final_data_2(self):
        self.assertEqual(calc2(open('data').readlines()), 290)

if __name__ == '__main__':
    unittest.main()
