import unittest
import re
#from collections import defaultdict
#from collections import Counter
#from numpy import sign

def calc2(data):
    calories = 0
    calories_list = list()
    for l in data:
        l = l.strip()
        if l == "":
            calories_list.append(calories)
            calories = 0
            continue
        calories += int(l)
    calories_list.append(calories)

    return sum(sorted(calories_list, reverse=True)[0:3])
    

def calc1(data):
    max_calories = 0
    calories = 0
    for l in data:
        l = l.strip()
        if l == "":
            calories = 0
            continue
        calories += int(l)
        max_calories = max(max_calories, calories)
        
    return max_calories

def read_sample():
    with open('sample_1') as f:
        lines = [line for line in f]
    return lines

def read_data():
    with open('data') as f:
        lines = [line for line in f]
    return lines

class TestDay(unittest.TestCase):

    def test_first_sample_data(self):
        self.assertEqual(calc1(read_sample()), 24000)

    def test_first_final_data(self):
        self.assertEqual(calc1(read_data()), 69836)

    def test_second_challenge_sample(self):
        self.assertEqual(calc2(read_sample()), 45000)

    def test_second_final_data_2(self):
        self.assertEqual(calc2(read_data()), 207968)

if __name__ == '__main__':
    unittest.main()
