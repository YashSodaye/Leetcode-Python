'''
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.


Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []
 
'''

def combination_sum(candidates, target):
    all_combinations = []
    def dfs(index, current_combination,current_sum):

        # If the current sum equals to the target, we've found a valid combination
        if current_sum == target:
            all_combinations.append(current_combination)
            return
        
        # If we've considered all candidates or the current sum exceeds the target, backtrack
        if index >= len(candidates) or current_sum > target:
            return
        
        dfs(index, current_combination + [candidates[index]], current_sum + candidates[index])
        dfs(index+1, current_combination,current_sum)

        # Start the DFS with an empty combination and sum of 0
    dfs(0,[],0)
        
    return all_combinations

print(combination_sum([2,3,6,7],7))

print(combination_sum(candidates = [2,3,5], target = 8))

print(combination_sum(candidates = [2], target = 1))

print(combination_sum(candidates = [1,2,3,2], target = 4))