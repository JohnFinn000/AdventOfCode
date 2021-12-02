import unittest

import day_1_1

class TestDay1(unittest.TestCase):
    def test_no_data(self):
        data = []
        self.assertEqual(day_1_1.calc(data), 0)

    def test_sample_data(self):
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(day_1_1.calc(data), 7)

if __name__ == '__main__':
    unittest.main()
