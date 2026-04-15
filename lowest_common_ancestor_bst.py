'''
235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.


Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # both nodes in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left

            # both nodes in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # split point (this is LCA)
            else:
                return root


# Helper: Insert into BST
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


# Helper: Find node by value
def find(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    elif val < root.val:
        return find(root.left, val)
    else:
        return find(root.right, val)


# ----------- TEST CASES ------------

if __name__ == "__main__":
    # Build BST from example
    values = [6, 2, 8, 0, 4, 7, 9, 3, 5]
    root = None
    for v in values:
        root = insert(root, v)

    sol = Solution()

    # Example 1
    p = find(root, 2)
    q = find(root, 8)
    lca = sol.lowestCommonAncestor(root, p, q)
    print("Example 1 LCA:", lca.val)  # Expected: 6

    # Example 2
    p = find(root, 2)
    q = find(root, 4)
    lca = sol.lowestCommonAncestor(root, p, q)
    print("Example 2 LCA:", lca.val)  # Expected: 2

    # Example 3
    root2 = TreeNode(2)
    root2.left = TreeNode(1)

    p = root2
    q = root2.left
    lca = sol.lowestCommonAncestor(root2, p, q)
    print("Example 3 LCA:", lca.val)  # Expected: 2