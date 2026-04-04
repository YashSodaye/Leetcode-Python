'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For easy printing
    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # Attach remaining nodes
        if list1:
            node.next = list1
        else:
            node.next = list2

        return dummy.next


# Helper function to convert list -> linked list
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Helper function to convert linked list -> list
def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ------------------- TEST CASES -------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print("Output 1:", linked_list_to_list(merged))  # [1,1,2,3,4,4]

    # Example 2
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    merged = sol.mergeTwoLists(list1, list2)
    print("Output 2:", linked_list_to_list(merged))  # []

    # Example 3
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    merged = sol.mergeTwoLists(list1, list2)
    print("Output 3:", linked_list_to_list(merged))  # [0]