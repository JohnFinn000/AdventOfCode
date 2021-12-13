import unittest

import day

class TestDay(unittest.TestCase):
    sample = [
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010",
]

    #def test_first_no_data(self):
    #    data = [0]
    #    self.assertEqual(day.calc_1(data), 0)

    def test_first_challenge_data(self):
        self.assertEqual(day.calc_1(self.sample), 198)

    #def test_second_no_data(self):
    #    data = []
    #    self.assertEqual(day.calc_2(data), 0)

    #def test_second_challenge_data(self):
    #    self.assertEqual(day.calc_2(self.sample), 230)

if __name__ == '__main__':
    unittest.main()
