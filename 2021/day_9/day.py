import unittest
import re
from collections import defaultdict
from collections import Counter
from numpy import sign

def calc(data):
    risk = 0
    data = map(lambda d: d.strip(), data)
    max_y = len(data)
    max_x = len(data[0])
    for x in range(0, max_x):
        for y in range(0, max_y):
            low_point = True
            for xa, ya in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
               if xa < 0 or xa >= max_x or ya < 0 or ya >= max_y:
                 continue
               if int(data[ya][xa]) <= int(data[y][x]):
                   low_point = False
            if low_point:
               risk += 1 + int(data[y][x])
    return risk

def bfs(basin, data, x, y):
    if int(data[y][x]) == 9:
        return
    

def calc2(data):
    data = map(lambda d: d.strip(), data)
    data_map = {}
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            data_map[(x,y)] = int(value)
    
    basin = {}
    basin_size = {}
    basins = []
    max_y = len(data)
    max_x = len(data[0])
    for x in range(0, max_x):
        for y in range(0, max_y):
            if data_map[(x,y)] < 9:
                if (x,y) in basin.keys():
                    continue
                else:
                    basin[(x,y)] = 1
                    basin_size = 1
                    queue = {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}
                    while len(queue):
                        me = queue.pop()
                        if me not in data_map.keys():
                            continue
                        elif data_map[me] == 9:
                            continue
                        elif me in basin.keys():
                            continue
                        else:
                            basin_size += 1
                            basin[me] = 1
                            xa = me[0]
                            ya = me[1]
                            queue.update({(xa-1, ya), (xa+1, ya), (xa, ya-1), (xa, ya+1)})
                    basins.append(basin_size)
    basins.sort(reverse=True)
    answer = 1
    for i in basins[0:3]:
        answer = answer * i
    return answer

class TestDay(unittest.TestCase):
    sample = [
"2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678",]

    def test_first_sample_data(self):
        self.assertEqual(calc(self.sample), 15)

    def test_first_final_data(self):
        self.assertEqual(calc(open('data').readlines()), 475)

    def test_second_sample_data(self):
        self.assertEqual(calc2(self.sample), 1134)

    def test_second_final_data_2(self):
        self.assertEqual(calc2(open('data').readlines()), 1092012)

if __name__ == '__main__':
    unittest.main()
