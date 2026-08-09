'''
208. Implement Trie (Prefix Tree)  

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
'''

class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}

        # Marks end of a complete word
        self.is_end = False


class Trie:
    def __init__(self):
        # Root node of Trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            # Create node if character not present
            if char not in node.children:
                node.children[char] = TrieNode()

            # Move to next node
            node = node.children[char]

        # Mark end of word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            # Character not found
            if char not in node.children:
                return False

            node = node.children[char]

        # Return True only if complete word exists
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            # Prefix not found
            if char not in node.children:
                return False

            node = node.children[char]

        return True


# ---------------- DRIVER CODE ---------------- #

if __name__ == "__main__":

    trie = Trie()

    print("Insert: apple")
    trie.insert("apple")

    print("search('apple'):", trie.search("apple"))     # True
    print("search('app'):", trie.search("app"))         # False
    print("startsWith('app'):", trie.startsWith("app")) # True

    print("\nInsert: app")
    trie.insert("app")

    print("search('app'):", trie.search("app"))         # True

    #print(Excellent)