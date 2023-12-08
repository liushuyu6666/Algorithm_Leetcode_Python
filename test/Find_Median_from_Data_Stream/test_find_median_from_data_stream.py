import unittest

from src.Find_Median_from_Data_Stream.find_median_from_data_stream_binary_search import MedianFinderBinarySearch
from src.Find_Median_from_Data_Stream.find_median_from_data_stream_heap import MedianFinderHeap


class TestMedianFinder(unittest.TestCase):
    def test_find_median_from_data_stream_binary_search(self):
        binary_search = MedianFinderBinarySearch()

        binary_search.addNum(1)
        binary_search.addNum(2)
        self.assertEqual(binary_search.findMedian(), 1.5)
        binary_search.addNum(3)
        self.assertEqual(binary_search.findMedian(), 2.0)

    def test_find_median_from_data_stream_heap(self):
        heap = MedianFinderHeap()

        heap.addNum(1)
        heap.addNum(2)
        self.assertEqual(heap.findMedian(), 1.5)
        heap.addNum(3)
        self.assertEqual(heap.findMedian(), 2.0)


if __name__ == "__main__":
    unittest.main()
