# algorithms
## quick select
QuickSelect is an algorithm designed to efficiently find the k-th smallest (or largest) element in an unordered list, representing a streamlined variant of the QuickSort algorithm. It operates with an expected linear time complexity.

QuickSelect follows a straightforward process. Initially, a pivot is selected randomly. Subsequently, all numbers are categorized into "larger," "equal," and "smaller" buckets. The "larger" bucket comprises elements greater than the pivot, and the same logic applies to the other two buckets. A recursive call is then made based on the bucket in which the k-th value is situated.