import unittest

import day_1_2

class TestDay2(unittest.TestCase):
    def test_no_data(self):
        data = []
        self.assertEqual(day_1_2.calc(data), 0)

    def test_sample_data(self):
        data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(day_1_2.calc(data), 5)

if __name__ == '__main__':
    unittest.main()
