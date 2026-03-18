'''
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

def threeSum(nums):
    # Check whether list is empty or less than 3 elements 
    if nums is None or len(nums) < 3:
        return []
    
    # Sort the list 
    nums.sort()

    # Unique triplet
    result = set()

    # Fix ith element and finding out other two elements
    
    for i in range(len(nums) - 2):
        left , right = i+1 , len(nums) - 1 

        while left < right:
            target = nums[i] + nums[left] + nums[right]

            if target == 0:
                result.add((nums[i],nums[left],nums[right]))
                left +=1
                right -=1
            elif target > 0 :
                right -=1
            else:
                left +=1
    return list(map(list,result))

print(threeSum([-1,0,1,2,-1,-4]))

print(threeSum([0,1,1]))

print(threeSum([0,0,0]))

print(threeSum([0,1]))

print(threeSum([]))