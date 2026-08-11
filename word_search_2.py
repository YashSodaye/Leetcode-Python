'''
212. Word Search II
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''


from typing import List


# Trie Node Definition
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:

    # Build Trie from words list
    def buildTrie(self, words):

        root = TrieNode()

        for word in words:

            node = root

            for char in word:

                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.is_end = True

        return root

    # DFS Search
    def dfs(self, board, node, i, j, path, result):

        # Boundary Conditions
        if (
            i < 0 or i >= len(board) or
            j < 0 or j >= len(board[0]) or
            board[i][j] not in node.children
        ):
            return

        char = board[i][j]

        next_node = node.children[char]

        path += char

        # Word Found
        if next_node.is_end:
            result.add(path)

            # Avoid duplicate results
            next_node.is_end = False

        # Mark current cell as visited
        board[i][j] = '#'

        # Explore 4 Directions
        directions = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1)
        ]

        for x, y in directions:
            self.dfs(board, next_node, x, y, path, result)

        # Backtrack
        board[i][j] = char

    # Main Function
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Step 1: Build Trie
        root = self.buildTrie(words)

        result = set()

        # Step 2: Start DFS from every cell
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] in root.children:
                    self.dfs(board, root, i, j, '', result)

        return list(result)


# ---------------- DRIVER CODE ---------------- #

if __name__ == "__main__":

    # Example 1
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]

    words = ["oath", "pea", "eat", "rain"]

    obj = Solution()

    ans = obj.findWords(board, words)

    print("Output:", ans)

    # Example 2
    board2 = [
        ["a", "b"],
        ["c", "d"]
    ]

    words2 = ["abcb"]

    ans2 = obj.findWords(board2, words2)

    print("Output:", ans2)


     # Example 3
    board3 = [
        ["a", "b", "e"],
        ["c", "d", "f"]
    ]

    words3 = ["abdf"]

    ans3 = obj.findWords(board3, words3)

    print("Output:", ans3)

     # Example 4
    board4 = [
        ["y", "a", "s"],
        ["o", "s", "h"],
        ["d", "a", "y"],
        ["s", "a", "e"]
    ]

    words4 = ["yash"]

    ans4 = obj.findWords(board4, words4)

    print("Output:", ans4)

    #print("GGs")