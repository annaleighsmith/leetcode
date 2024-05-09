"""
An aggregation of linked list problems from LeetCode with added methods
and helper functions for print debugging and learning 
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}->{self.next}"


class LinkedList:
    def __init__(self, nums: Optional[List[int]], head: Optional[ListNode] = None):
        if not nums and not head:
            raise ValueError("A list of ints or a head node must be provided")

        if head:
            self.head = head
        elif nums:
            self.head = ListNode(nums[0])
            current = self.head
            for num in nums[1:]:
                current.next = ListNode(num)
                current = current.next

    def __str__(self) -> str:
        current = self.head
        nums = []
        while current:
            nums.append(str(current.val))
            current = current.next
        return "->".join(nums)

    def get_node(self, idx):
        current = self.head
        for i in range(idx):
            current = current.next
        return current


def delete_node(node: ListNode):
    """
    Given a node that is not the tail in a singularly linked list
    modify the linked list the node belongs to so that the given
    element is deleted

    Return nothing, modify in place

    Time complexity O(1)
    Space complexity O(1)
    """
    node.val = node.next.val
    node.next = node.next.next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given the head of a singly linked list, reverse the list
    and return the reversed list

    Current nodes next needs to be the previous nodes value

    Using an interative approach

    Time complexity O(n)
    Space complexity O(1)
    """
    previous = None
    while head:
        next_item = head.next

        if previous is None:
            head.next = None
        else:
            head.next = previous

        previous = head
        head = next_item  # next node assignment
    return previous


def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Given two sorted lists merge them into one sorted list.
    Return the head of the merged linked list

    Time Complexity O(n+m)
    Space Complexity O(1)
    """
    if not list1 and not list2:
        return list1
    if not list1 or not list2:
        return list1 if not list2 else list2

    seek, target = (
        (list1, list2) if list1.val < list2.val else (list2, list1)
    )  # ascending
    head = seek
    while seek and target:
        while seek.next and seek.next.val < target.val:
            seek = seek.next
        seek.next, target = target, seek.next
        seek = seek.next
    return head


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Given a non-empty singly linked list, return the middle node
    If there are two middle nodes, return the second middle node
    """
    head_copy = head
    len = 0
    while head:
        len += 1
        head = head.next
    mid = len // 2

    idx = 0
    while head_copy:
        if idx == mid:
            return head_copy
        else:
            idx += 1
            head_copy = head_copy.next


def middle_node_two_pointers(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def solve237():
    listA = LinkedList([4, 5, 1, 9])
    print(listA)
    delete_node(listA.get_node(1))
    print(listA)


def solve206():
    listB = LinkedList([1, 2, 3, 4, 5])
    print(listB)
    res = reverse_list(listB.head)
    listC = LinkedList(None, res)
    print(listC)


def solve21():
    list1 = LinkedList([1, 2, 4])
    list2 = LinkedList([1, 3, 4])
    res = merge_two_lists(list1.head, list2.head)
    list3 = LinkedList(None, res)
    print(list3)


def solve876():
    list1 = LinkedList([1, 2, 3, 4, 5, 6])
    res = middle_node(list1.head)
    print(res)
    list2 = LinkedList(None, res)
    print(list2)


if __name__ == "__main__":
    solve876()
