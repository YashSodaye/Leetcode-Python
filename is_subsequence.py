'''
392. Is Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

def is_subsequence(s,t):
    itr1 , itr2 = 0,0

    while itr1 < len(s) and itr2 < len(t):
        if s[itr1] == t[itr2]:
            itr1 +=1
            itr2 +=1
        else:
            itr2 +=1
        
    return itr1 == len(s)

print(is_subsequence("abc","ahbgdc"))

print(is_subsequence("axc","ahbgdc"))

print("Hello")