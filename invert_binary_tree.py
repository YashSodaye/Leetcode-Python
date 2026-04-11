'''
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:

Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
'''

from collections import deque

# Tree Node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Correct build_tree (level-order)
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# Invert Tree
def invertTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


# Convert tree to list (level-order)
def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # remove trailing None
    while result and result[-1] is None:
        result.pop()

    return result


# -------- TESTS --------
root = build_tree([4,2,7,1,3,6,9])
print(tree_to_list(invertTree(root)))  # ✅ [4,7,2,9,6,3,1]

root2 = build_tree([2,1,3])
print(tree_to_list(invertTree(root2)))  # ✅ [2,3,1]

root3 = build_tree([])
print(tree_to_list(invertTree(root3)))  # ✅ []