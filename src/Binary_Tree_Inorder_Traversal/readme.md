# algorithms
## tree
### binary tree
#### inorder traversal

The sequence of inorder traversal in a binary tree is depicted in the illustration below:
![inorder traversal](inorder_traversal.png)

To simplify, the traversal order follows the sequence of the left subtree, the current node, and its right subtree.

##### recursion in inorder traversal
The recursive pattern for traversing the tree in the inorder fashion is as follows:
```python
from typing import Optional
import TreeNode

def inorder(node: Optional[TreeNode]) -> None:
    if node:
        inorder(node.left)
        # handle with the current node
        inorder(node.right)
```
This recursive approach ensures that the left subtree is traversed first, followed by the current node, and finally, the right subtree.

##### stack in inorder traversal
A stack can serve as an alternative to the recursive approach.
