import unittest
from src.Car_Pooling.car_pooling_sorting import CarPoolingSorting
from src.Car_Pooling.car_pooling_diffs_array import CarPoolingDifferencesArray
from src.Car_Pooling.car_pooling_min_heap import CarPoolingMinHeap


class TestCarPooling(unittest.TestCase):
    def test_car_pooling_sorting(self):
        car = CarPoolingSorting()

        trips, capacity = [[2, 1, 5], [3, 3, 7]], 4
        self.assertEqual(car.carPooling(trips, capacity), False)

        trips, capacity = [[2, 1, 5], [3, 3, 7]], 5
        self.assertEqual(car.carPooling(trips, capacity), True)

        trips, capacity = [[2, 1, 5], [3, 5, 7]], 3
        self.assertEqual(car.carPooling(trips, capacity), True)

    def test_car_pooling_no_sorting(self):
        car = CarPoolingDifferencesArray()

        trips, capacity = [[2, 1, 5], [3, 3, 7]], 4
        self.assertEqual(car.carPooling(trips, capacity), False)

        trips, capacity = [[2, 1, 5], [3, 3, 7]], 5
        self.assertEqual(car.carPooling(trips, capacity), True)

        trips, capacity = [[2, 1, 5], [3, 5, 7]], 3
        self.assertEqual(car.carPooling(trips, capacity), True)

    def test_car_pooling_min_heap(self):
        car = CarPoolingMinHeap()

        trips, capacity = [[2, 1, 5], [3, 3, 7]], 4
        self.assertEqual(car.carPooling(trips, capacity), False)

        trips, capacity = [[2, 1, 5], [3, 3, 7]], 5
        self.assertEqual(car.carPooling(trips, capacity), True)

        trips, capacity = [[2, 1, 5], [3, 5, 7]], 3
        self.assertEqual(car.carPooling(trips, capacity), True)