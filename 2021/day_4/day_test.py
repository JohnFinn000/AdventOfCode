import unittest

row = int("11111", 2)
col = int("00001" * 5, 2)

def bitboard_validate(bitboard):
  for i in range(5):
    for mask in [row << 5*i, col << i]:
        if (bitboard & mask) == mask:
            return True
  return False

def bitboard_coord(coords):
  return 1 << coords[0] + (coords[1] * 5)

def bitboard_print(bb):
  for i in range(5):
    print("{0:05b}".format(bb & row))
    bb >>= 5

def calc_1(data):
  picks = map(int, data[0].split(","))
  print picks
 
  boards = []
  bitboards = []
  x, y = 0, 0
  for l in data[1:]:
    if l.strip() == "":
        y = 0
        boards.append(dict())
        bitboards.append(0)
        continue
    x = 0
    for n in l.split():
        boards[-1][int(n)] = (x, y)
        x += 1
    y += 1

  for p in picks:
    for i in range(0, len(boards)):
      try:
        bitboards[i] |= bitboard_coord(boards[i][p])
        del boards[i][p]
        if bitboard_validate(bitboards[i]):
            bitboard_print(bitboards[i])
            return sum(iter(boards[i].keys())) * p
      except KeyError:
        pass
  
  
  return -1

def calc_2(data):
  picks = map(int, data[0].split(","))
  print picks
 
  boards = []
  bitboards = []
  x, y = 0, 0
  for l in data[1:]:
    if l.strip() == "":
        y = 0
        boards.append(dict())
        bitboards.append(0)
        continue
    x = 0
    for n in l.split():
        boards[-1][int(n)] = (x, y)
        x += 1
    y += 1

  winners = dict()
  final_score = 0
  for p in picks:
    for i in range(0, len(boards)):
      try:
        if bitboard_validate(bitboards[i]):
            continue
        bitboards[i] |= bitboard_coord(boards[i][p])
        del boards[i][p]
        if bitboard_validate(bitboards[i]):
            final_score = sum(iter(boards[i].keys())) * p
            print "Board %r wins with a final score %r" % (i, final_score)
            print "%r %r" % (sum(iter(boards[i].keys())), p)
            bitboard_print(bitboards[i])
      except KeyError:
        pass
  return final_score

class TestDay(unittest.TestCase):
    sample = [
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
 "8  2 23  4 24",
"21  9 14 16  7",
 "6 10  3 18  5",
 "1 12 20 15 19",
"",
 "3 15  0  2 22",
 "9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
 "2  0 12  3  7",
]

    def test_first_challenge_data(self):
        self.assertEqual(calc_1(self.sample), 4512)

    def test_final_data(self):
        self.assertEqual(calc_1(open('data').readlines()), 67716)

    def test_second_challenge_sample(self):
        self.assertEqual(calc_2(self.sample), 1924)

    def test_final_data_2(self):
        self.assertEqual(calc_2(open('data').readlines()), 1830)

if __name__ == '__main__':
    unittest.main()
