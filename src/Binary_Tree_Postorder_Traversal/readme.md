# algorithms
## tree
### binary tree
#### postorder traversal
##### stack in postorder traversal
A stack can serve as an alternative to the recursive approach.

Two key points to consider when using a stack for postorder traversal:

- The right subtree should be pushed into the stack first due to the Last In, First Out (LIFO) nature.
- As a consequence of the first point, the left subtree must be pushed into the stack beforehand.
