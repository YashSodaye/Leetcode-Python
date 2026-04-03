'''
3661. Maximum Walls Destroyed by Robots

There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
Robots are not destroyed by bullets.
 

Example 1:

Input: robots = [4], distance = [3], walls = [1,10]

Output: 1

Explanation:

robots[0] = 4 fires left with distance[0] = 3, covering [1, 4] and destroys walls[0] = 1.
Thus, the answer is 1.
Example 2:

Input: robots = [10,2], distance = [5,1], walls = [5,2,7]

Output: 3

Explanation:

robots[0] = 10 fires left with distance[0] = 5, covering [5, 10] and destroys walls[0] = 5 and walls[2] = 7.
robots[1] = 2 fires left with distance[1] = 1, covering [1, 2] and destroys walls[1] = 2.
Thus, the answer is 3.
Example 3:
Input: robots = [1,2], distance = [100,1], walls = [10]

Output: 0

Explanation:

In this example, only robots[0] can reach the wall, but its shot to the right is blocked by robots[1]; thus the answer is 0.

'''

from typing import List
from bisect import bisect_left
from functools import cache

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0

            # Fire left
            left = arr[i][0] - arr[i][1]
            if i > 0:
                left = max(left, arr[i - 1][0] + 1)

            l = bisect_left(walls, left)
            r = bisect_left(walls, arr[i][0] + 1)
            ans = dfs(i - 1, 0) + (r - l)

            # Fire right
            right = arr[i][0] + arr[i][1]
            if i + 1 < n:
                if j == 0:
                    right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
                else:
                    right = min(right, arr[i + 1][0] - 1)

            l = bisect_left(walls, arr[i][0])
            r = bisect_left(walls, right + 1)
            ans = max(ans, dfs(i - 1, 1) + (r - l))

            return ans

        ans = dfs(n - 1, 1)
        dfs.cache_clear()
        return ans


# ------------------- DRIVER CODE -------------------
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    robots = [4]
    distance = [3]
    walls = [1, 10]
    print("Output 1:", sol.maxWalls(robots, distance, walls))  # Expected: 1

    # Test Case 2
    robots = [10, 2]
    distance = [5, 1]
    walls = [5, 2, 7]
    print("Output 2:", sol.maxWalls(robots, distance, walls))  # Expected: 3

    # Test Case 3
    robots = [1, 2]
    distance = [100, 1]
    walls = [10]
    print("Output 3:", sol.maxWalls(robots, distance, walls))  # Expected: 0