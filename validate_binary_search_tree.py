'''
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # List to store in-order traversal
        io_list = []
        self.helper(root, io_list)

        # Edge case: empty tree
        if not io_list:
            return True

        prev = io_list[0]

        for i in range(1, len(io_list)):
            if io_list[i] <= prev:
                return False
            prev = io_list[i]

        return True

    def helper(self, tree_node, io_list):
        if tree_node is None:
            return

        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)


# ----------- Helper to build tree from list -----------
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


# ----------- Test Cases -----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = build_tree([2, 1, 3])
    print("Example 1:", sol.isValidBST(root1))  # Expected: True

    # Example 2
    root2 = build_tree([5, 1, 4, None, None, 3, 6])
    print("Example 2:", sol.isValidBST(root2))  # Expected: False

    # Additional test
    root3 = build_tree([10, 5, 15, None, None, 6, 20])
    print("Example 3:", sol.isValidBST(root3))  # Expected: False Positive

    # Extras