'''
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, index):

            # Reached end of word
            if index == len(word):
                return node.is_end

            char = word[index]

            # Wildcard case
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            # Normal character case
            if char in node.children:
                return dfs(node.children[char], index + 1)

            return False

        return dfs(self.root, 0)


# -------------------------
# Driver Code (VS Code Run)
# -------------------------

if __name__ == "__main__":

    wordDictionary = WordDictionary()

    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    print(wordDictionary.search("pad"))   # False
    print(wordDictionary.search("bad"))   # True
    print(wordDictionary.search(".ad"))   # True
    print(wordDictionary.search("b.."))   # True