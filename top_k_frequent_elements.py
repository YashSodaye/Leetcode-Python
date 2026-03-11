'''
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

'''

def topKFrequent(nums,k):

    #Intitalize Bucket
    bucket = [[] for _ in range(len(nums)+1)]
    frequencyMap = {}

    #FrequencyMap
    for n in nums:
        if n not in frequencyMap:
            frequencyMap[n] = 1
        else:
            frequencyMap[n] +=1
    
    #Filling Bucket
    for key,frequency in frequencyMap.items():
        bucket[frequency].append(key)

    #Iterate Bucket in reverse to get top K frequent elements

    result = []

    for i in reversed(range(len(bucket))):
        if bucket[i]:
            for value in bucket[i]:
                if len(result) <k:
                    result.append(value)
                else:
                    return result
                
    return result

print(topKFrequent([1,1,1,2,2,3], 2))

print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))

print(topKFrequent([1], 1))