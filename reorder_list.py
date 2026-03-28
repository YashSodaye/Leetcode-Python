'''
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 
Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list
# Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    if not head or not head.next:
        return head

    # Step 1: Find middle
    slow, fast = head, head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Cut list
    prev.next = None

    # Step 2: Reverse second half
    prev_node = None
    curr = slow

    while curr:
        next_temp = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_temp

    # Step 3: Merge safely
    first, second = head, prev_node

    while first and second:
        temp1 = first.next
        temp2 = second.next

        first.next = second

        # IMPORTANT: avoid cycle / crash
        if temp1 is None:
            break

        second.next = temp1

        first = temp1
        second = temp2

    return head


# Helper functions
def create_list(arr):
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Test
head = create_list([1, 2, 3, 4, 5])

print("Before:")
print_list(head)

reorderList(head)

print("After:")
print_list(head)