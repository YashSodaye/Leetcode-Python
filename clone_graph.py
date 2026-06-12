'''
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

'''
# clone_graph.py

from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to store original node -> cloned node
        cloned_nodes = {}

        # Create clone for first node
        cloned_nodes[node] = Node(node.val)

        # BFS queue
        queue = deque([node])

        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:

                # If neighbor not cloned yet
                if neighbor not in cloned_nodes:
                    cloned_nodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add cloned neighbor to cloned current node
                cloned_nodes[current_node].neighbors.append(
                    cloned_nodes[neighbor]
                )

        return cloned_nodes[node]


# ---------------- TESTING ----------------

def print_graph(node):
    """Print graph using BFS"""
    visited = set()
    queue = deque([node])

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        neighbors = [n.val for n in current.neighbors]
        print(f"Node {current.val} -> {neighbors}")

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)


# Create sample graph
# Graph:
# 1 -- 2
# |    |
# 4 -- 3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

print("Original Graph:")
print_graph(node1)

# Clone graph
solution = Solution()
cloned_graph = solution.cloneGraph(node1)

print("\nCloned Graph:")
print_graph(cloned_graph)

print("Well Done")

print("Working fine")