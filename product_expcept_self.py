'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

def productExceptSelf(nums):
    n = len(nums)

    #Array to store all left multiplication
    left = [1] * n
    for i in range(1,n):
        left[i] = left[i-1] * nums[i-1]
    
    #Array to store all right multiplication
    right = [1] * n 
    for i in range(n-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]

    result = [1] * n
    for i in range(n):
        result[i] = left[i] * right[i]

    return result


print(productExceptSelf([1,2,3,4]))

print(productExceptSelf([-1,1,0,-3,3]))
    