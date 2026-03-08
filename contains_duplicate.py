'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
'''

def contains_duplicate(nums):
    hashmap = {}

    for i in range(len(nums)):
        if nums[i] in hashmap:
            return True
        hashmap[nums[i]] = 1
    return False

print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))