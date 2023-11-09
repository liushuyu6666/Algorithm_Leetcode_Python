# Algorithms
## Greedy Algorithm in differences array
This algorithm is employed for solving LeetCode problems [1552. Magnetic Force Between Two Balls
](https://leetcode.com/problems/magnetic-force-between-two-balls/description/) and [2517. Maximum Tastiness of Candy Basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/).

In this context, with an array `arr` and an integer `x`, the objective is to maximize the number of selected elements while ensuring that the minimum absolute difference between any two chosen elements is equal to or greater than `x`.

For instance, consider the array `arr = [1, 2, 5, 8, 13, 21]`. When `x = 3`, the algorithm aims to select elements such as `[1, 5, 8, 13, 21]`, where the absolute differences between any two selected elements are equal to or greater than 3. Similarly, when `x = 8`, the goal is to pick elements like `[1, 13, 21]`.

This type of question exhibits a key property: The position of elements does not influence the selection process.

To address this problem, the array is sorted in ascending order to obtain a `sorted` array. This sorting ensures that for a certain element `a`, two adjacent elements `b` and `c` has smaller differences to `a`. For instance, if we select `element[0]`, `element[4]`, and `element[6]` with the condition `abs(element[0] - element[4]) >= x` and `abs(element[4] - element[6]) >= x`, it implies `abs(element[0] - element[6]) >= x`. 

Subsequently, differences between nearby elements are calculated upon the `sorted`, resulting in a `diffs` array, which is one element shorter than the original array. Now the difference is cumulative on this `diffs` array.

Due to the implementation of the greedy algorithm, the initial selection should always be the first element from the `sorted` array. Subsequently, accumulation along the `diffs` array is performed. Each time the cumulative value reaches or exceeds `x`, the corresponding element is selected.