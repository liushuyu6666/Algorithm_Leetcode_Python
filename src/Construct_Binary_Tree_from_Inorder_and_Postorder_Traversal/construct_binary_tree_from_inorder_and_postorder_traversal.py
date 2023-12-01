from typing import List, Optional

from src.Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal.TreeNode import TreeNode


def split_inorder(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not postorder:
        return None

    curr_val = postorder.pop()
    val_index = inorder.index(curr_val)
    curr_node = TreeNode(val=curr_val)
    left_inorder = inorder[0 : val_index]
    right_inorder = inorder[val_index + 1 :]
    curr_node.right = split_inorder(right_inorder, postorder)
    curr_node.left = split_inorder(left_inorder, postorder)

    return curr_node


class ConstructBinaryTreeFromInorderAndPostorderTraversal:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return split_inorder(inorder, postorder)
