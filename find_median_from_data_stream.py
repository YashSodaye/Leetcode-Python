'''
295. Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''

import heapq


class MedianFinder:
    def __init__(self):
        # Max heap (store negative values)
        self.left_half = []

        # Min heap
        self.right_half = []

    def addNum(self, num: int) -> None:

        # Add number to appropriate heap
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
        else:
            heapq.heappush(self.right_half, num)

        # Rebalance heaps
        if len(self.left_half) > len(self.right_half) + 1:
            moved = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, moved)

        elif len(self.right_half) > len(self.left_half):
            moved = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -moved)

    def findMedian(self) -> float:

        # If odd number of elements
        if len(self.left_half) > len(self.right_half):
            return float(-self.left_half[0])

        # If even number of elements
        return (-self.left_half[0] + self.right_half[0]) / 2.0


# -----------------------------
# VS Code Runnable Test
# -----------------------------
if __name__ == "__main__":

    medianFinder = MedianFinder()

    medianFinder.addNum(1)
    print("Added 1")

    medianFinder.addNum(2)
    print("Added 2")

    print("Median:", medianFinder.findMedian())  # 1.5

    medianFinder.addNum(3)
    print("Added 3")

    print("Median:", medianFinder.findMedian())  # 2.0