import unittest
from src.Add_Bold_Tag_in_String.add_bold_tag_in_string import AddBoldTagInString


class TestAddBoldTagInString(unittest.TestCase):
    def test_add_bold_in_string(self):
        bold = AddBoldTagInString()

        # s, words = "abcxyz123", ["abc","123"]
        # self.assertEqual(bold.addBoldTag(s, words), "<b>abc</b>xyz<b>123</b>")

        s, words = "aaabbb", ["aa", "b"]
        self.assertEqual(bold.addBoldTag(s, words), "<b>aaabbb</b>")