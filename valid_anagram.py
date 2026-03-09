'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

'''

def valid_anagram(s,t):

    s = s.lower()
    t = t.lower()

    s = s.replace(" ", "")
    t = t.replace(" ", "")

    if len(s) != len(t):
        return False
    
    counts = [0] * 26

    for char in s:
        counts[ord(char) - ord('a')] += 1

    for char in t:
        counts[ord(char) - ord('a')] -= 1

    for count in counts:
        if count !=0:
            return False
        
    return True
        
    
print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))
