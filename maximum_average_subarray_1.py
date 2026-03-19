'''
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''

def findMaxAverage(nums, k):
    
    # Sum of Starting Window 
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]

    max_sum = current_sum

    # Start Sliding Window
    start_index = 0
    end_index = k

    while end_index < len(nums):

        # Removing previous element
        current_sum -= nums[start_index]
        start_index +=1

        # Adding next element 
        current_sum += nums[end_index]
        end_index +=1

        # Update Max Sum
        max_sum = max(current_sum, max_sum)

    # Return the average
    return max_sum / k

print(findMaxAverage([1,12,-5,-6,50,3], 4))

print(findMaxAverage([5], 1))