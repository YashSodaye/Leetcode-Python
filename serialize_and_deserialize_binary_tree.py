'''
297. Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        queue = [root]
        result = []
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")
        
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        
        while queue:
            node = queue.pop(0)
            
            if i < len(values) and values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root


# Helper function to print tree in level-order (for testing)
def print_tree(root):
    if not root:
        print([])
        return
    
    queue = [root]
    result = []
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    print(result)


# ----------- TESTING -----------
if __name__ == "__main__":
    # Build example tree: [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()

    serialized = codec.serialize(root)
    print("Serialized:", serialized)

    deserialized = codec.deserialize(serialized)
    print("Deserialized tree (level-order):")
    print_tree(deserialized)
