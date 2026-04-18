'''
230. Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
 

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1


Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        io_list = []
        self.helper(root, io_list)
        return io_list[k - 1]

    def helper(self, tree_node, io_list):
        if tree_node is None:
            return

        self.helper(tree_node.left, io_list)
        io_list.append(tree_node.val)
        self.helper(tree_node.right, io_list)

# Helper function to build tree from level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# ----------- TEST CASES -----------

# Example 1
root1 = build_tree([3, 1, 4, None, 2])
k1 = 1
print("Output 1:", Solution().kthSmallest(root1, k1))  # Expected: 1

# Example 2
root2 = build_tree([5, 3, 6, 2, 4, None, None, 1])
k2 = 3
print("Output 2:", Solution().kthSmallest(root2, k2))  # Expected: 3