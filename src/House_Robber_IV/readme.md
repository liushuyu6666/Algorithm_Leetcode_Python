# Types
## Minimize the maximum value
In this problem, the 'capability' is defined as the maximum amount of money the robber can steal from a single house among all the houses they rob. The goal is to minimize this capability, making it a 'minimized maximum value' problem.

To tackle this type of problem, we employ a binary search approach. We begin by assuming that the thief intends to steal a specific amount, denoted as 'x', and we want to determine the maximum number of houses he can rob under this amount, denoted as 'numsOfHouses'. We establish a function, denoted as $numsOfHouses = f(x)$, to represent this relationship.

We use a greedy algorithm to calculate the 'numsOfHouses' function, and then we apply a binary search algorithm to find the minimum value of 'x' that results in 'numsOfHouses' being greater than or equal to a given threshold `k`.


# Algorithms
## Binary Search
In this context, the middle value is determined by the 'numsOfHouses' function. If `numsOfHouses(x)` is greater than or equal to `k`, it signifies that the robbed money can be reduced, and, consequently, the right pointer should be moved to left.

## Greedy Algorithm
To determine the maximum number of houses that can be robbed under a specified amount `x`, we employ a greedy algorithm. As we traverse the entire array, our approach is to prioritize robbing houses at the earliest opportunity, optimizing the overall outcome.