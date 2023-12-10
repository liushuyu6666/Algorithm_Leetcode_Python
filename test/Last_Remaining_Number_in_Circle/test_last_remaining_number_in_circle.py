import unittest

from src.Last_Remaining_Number_in_Circle.last_remaining_number_in_circle_zero_indexed import Josephuse

class TestJosephuse(unittest.TestCase):
    def test_zero_indexed(self):
        josephuse = Josephuse()

        index = josephuse.zero_indexed(7, 4)
        self.assertEqual(index, 1)

        index = josephuse.one_indexed(7, 4)
        self.assertEqual(index, 1)

