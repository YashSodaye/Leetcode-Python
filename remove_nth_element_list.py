'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to remove Nth node from end
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    slow, fast = dummy, dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Delete node
    slow.next = slow.next.next

    return dummy.next


# Helper: Create linked list from array
def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# Helper: Print linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# 🔥 TEST CASES
if __name__ == "__main__":
    # Example 1
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Before:")
    print_list(head)

    head = removeNthFromEnd(head, 2)

    print("After removing 2nd from end:")
    print_list(head)

    # Example 2
    head2 = create_linked_list([1])
    print("\nBefore:")
    print_list(head2)

    head2 = removeNthFromEnd(head2, 1)

    print("After removing 1st from end:")
    print_list(head2)

    # Example 3
    head3 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    print("Before:")
    print_list(head3)

    head3 = removeNthFromEnd(head3, 3)

    print("After removing 3rd from end:")
    print_list(head3)