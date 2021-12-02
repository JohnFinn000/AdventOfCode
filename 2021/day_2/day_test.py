import unittest

import day

class TestDay(unittest.TestCase):
    sample = [
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2",
]

    def test_first_no_data(self):
        data = []
        self.assertEqual(day.calc_1(data), 0)

    def test_first_challenge_data(self):
        self.assertEqual(day.calc_1(self.sample), 150)

    def test_second_no_data(self):
        data = []
        self.assertEqual(day.calc_2(data), 0)

    def test_second_challenge_data(self):
        self.assertEqual(day.calc_2(self.sample), 900)

if __name__ == '__main__':
    unittest.main()
