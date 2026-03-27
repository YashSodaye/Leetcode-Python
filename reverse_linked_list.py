'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''

from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reverse Linked List Function
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

# helper to create list
def create(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for x in arr[1:]:
        curr.next = ListNode(x)
        curr = curr.next
    return head

# helper to print list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = create([1,2,3,4,5])
new_head = reverseList(head)
print_list(new_head)