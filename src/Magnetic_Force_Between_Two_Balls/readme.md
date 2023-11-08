# Caveats
## Calculate the difference within an array for greedy algorithm
In this context, the placement of baskets does not impact the outcome. This is because, regardless of their positions, the magnetic force between two baskets always equates to $|basket1 - basket2|$. The greedy algorithm begins its iteration from the initial element in the `diffs` array, accumulating magnetic force. Therefore, the maximum possible magnetic force must be equal to `sum(diffs)`.

For instance, consider a `position` array `[3, 2, 1, 100]`. Without sorting the array, the `diffs` become `[1, 1, 1, 99]`, resulting in an incorrect largest magnetic force when using the greedy algorithm, which would be 102.