'''
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
'''

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case: if both trees are empty
        if p is None and q is None:
            return True
        
        # Trees are not the same if either is empty or values differ
        if p is None or q is None or p.val != q.val:
            return False

        # Recursively check left and right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

# Helper function to build tree from list (level-order)
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

# ---- Test cases ----
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print("Example 1:", sol.isSameTree(p1, q1))  # True

    # Example 2
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print("Example 2:", sol.isSameTree(p2, q2))  # False

    # Example 3
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print("Example 3:", sol.isSameTree(p3, q3))  # False