import unittest

from src.Kth_Largest_Element_in_an_Array.kth_largest_element_in_an_array import KthLargestElementInAnArray
from src.Kth_Largest_Element_in_an_Array.kth_largest_element_in_an_array_quick_select \
    import KthLargestElementInAnArrayQuickSelect


class TestKthLargestElementInAnArray(unittest.TestCase):
    def test_kth(self):
        kth_largest = KthLargestElementInAnArray()

        # Test case 1: Example case
        nums, k = [3, 2, 1, 5, 6, 4], 2
        self.assertEqual(kth_largest.findKthLargest(nums, k), 5)

        # Test case 2: Example case
        nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
        self.assertEqual(kth_largest.findKthLargest(nums, k), 4)

    def test_kth_using_quick_select(self):
        kth_largest_quick_select = KthLargestElementInAnArrayQuickSelect()

        # Test case 1: Example case
        nums, k = [3, 2, 1, 5, 6, 4], 2
        self.assertEqual(kth_largest_quick_select.findKthLargest(nums, k), 5)

        # Test case 2: Example case
        nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
        self.assertEqual(kth_largest_quick_select.findKthLargest(nums, k), 4)


if __name__ == "__main__":
    unittest.main()
