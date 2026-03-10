'''
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

'''

def groupAnagrams(strs):
        if not strs:
            return []

        hashmap = {}

        def get_frequency_string(element):
            freq_list = [0] * 26

            for char in element:
                freq_list[ord(char) - ord('a')] += 1

            frequency_string = []
            char = 'a'

            for position in freq_list:
                frequency_string.append(char)
                frequency_string.append(str(position))
                char = chr(ord(char) + 1)

            return ''.join(frequency_string)

        for element in strs:
            frequency_string = get_frequency_string(element)

            if frequency_string not in hashmap:
                hashmap[frequency_string] = []

            hashmap[frequency_string].append(element)

        return list(hashmap.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

print(groupAnagrams([""]))

print(groupAnagrams(["a"]))