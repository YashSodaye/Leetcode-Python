'''
128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
'''

def longestConsecutive(nums):
    longest_length = 0
    hashmap = {}

    #Populate the hashmap with all the numbers and marked as not traveled
    for num in nums:
        hashmap[num] = False

    for num in nums:
        current_length = 1

        #Check for forward direction
        next_num = num + 1
        while next_num in hashmap and not hashmap[next_num]:
            current_length +=1
            hashmap[next_num] = True
            next_num +=1

        #Check for backward direction
        prev_num = num - 1
        while prev_num in hashmap and not hashmap[prev_num]:
            current_length +=1
            hashmap[prev_num] = True
            prev_num -=1    

        longest_length = max(longest_length, current_length)
    
    return longest_length

print(longestConsecutive([100,4,200,1,3,2]))
    
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

print(longestConsecutive([1,0,1,2]))