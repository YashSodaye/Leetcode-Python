'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head

def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def middleNode(head):
    # Initialize slow and fast pointer
    slow, fast = head, head

    # Traverse as long as fast and its next node are not null
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    # Loop ends, slow pointer will be at the middle of the list
    return slow

head_1 = create_linked_list([1,2,3,4,5])

head_2 = create_linked_list([1,2,3,4,5,6])

head_3 = (create_linked_list([1,2,3]))

print(print_list(middleNode(head_1)))

print(print_list(middleNode(head_2)))

print(print_list(middleNode(head_3)))