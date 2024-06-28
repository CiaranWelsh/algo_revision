"""
Two Pointer Technique Examples

This module demonstrates various categories of the two-pointer technique with examples.
Each function includes a detailed docstring explaining the problem statement, the category of the two-pointer technique,
a detailed description of the algorithm, and the time and space complexity analysis.
"""

def two_sum_sorted(arr, target):
    """
    Find a pair with a given sum in a sorted array.

    Problem Statement:
    Given a sorted array `arr` and a target sum `target`, find two numbers in the array that add up to `target`.

    Category: Opposite Direction Pointers

    Algorithm Description:
    - Initialize two pointers, one at the beginning (`left`) and one at the end (`right`) of the array.
    - Calculate the sum of the elements at these two pointers.
    - If the sum equals the target, return the pair.
    - If the sum is less than the target, move the `left` pointer to the right to increase the sum.
    - If the sum is greater than the target, move the `right` pointer to the left to decrease the sum.
    - Repeat until the pointers meet or cross each other.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This approach is more efficient than the brute force approach, which has a time complexity of O(n^2).
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None  # No pair found


def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array in-place.

    Problem Statement:
    Given a sorted array `arr`, remove the duplicates in-place such that each element appears only once and return the new length.

    Category: Same Direction Pointers

    Algorithm Description:
    - Initialize a `write_index` to keep track of the position to write the next unique element.
    - Iterate through the array with a pointer `i`.
    - If the current element is different from the previous element, write it at the `write_index` and increment the `write_index`.
    - Continue until the end of the array.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This approach is more efficient than the brute force approach, which would require additional space to store the unique elements.
    """
    if not arr:
        return 0

    write_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index


def reverse_string(s):
    """
    Reverse a string using the two-pointer technique.

    Problem Statement:
    Given a string `s`, reverse it using the two-pointer technique.

    Category: Opposite Direction Pointers

    Algorithm Description:
    - Convert the string to a list to allow modification.
    - Initialize two pointers, one at the beginning (`left`) and one at the end (`right`) of the list.
    - Swap the elements at these two pointers.
    - Move the `left` pointer to the right and the `right` pointer to the left.
    - Repeat until the pointers meet or cross each other.
    - Convert the list back to a string and return it.

    Time Complexity: O(n)
    Space Complexity: O(n) due to the conversion of the string to a list and back.

    This approach is more efficient than the brute force approach, which would involve creating a new string by iterating from the end.
    """
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)


def max_area(height):
    """
    Find the container with the most water.

    Problem Statement:
    Given an array `height` where `height[i]` represents the height of a vertical line at index `i`, find two lines that together with the x-axis form a container that holds the most water.

    Category: Opposite Direction Pointers

    Algorithm Description:
    - Initialize two pointers, one at the beginning (`left`) and one at the end (`right`) of the array.
    - Calculate the area formed by the lines at these two pointers and the x-axis.
    - Update the maximum area if the current area is larger.
    - Move the pointer pointing to the shorter line towards the other pointer to potentially find a larger area.
    - Repeat until the pointers meet or cross each other.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This approach is more efficient than the brute force approach, which has a time complexity of O(n^2).
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    Problem Statement:
    Given a string `s`, find the length of the longest substring without repeating characters.

    Category: Same Direction Pointers

    Algorithm Description:
    - Use a set to keep track of characters in the current window.
    - Initialize two pointers, `left` and `right`, both starting at the beginning of the string.
    - Move the `right` pointer to expand the window and add characters to the set.
    - If a character is already in the set, move the `left` pointer to shrink the window until the character is removed from the set.
    - Keep track of the maximum length of the window during this process.

    Time Complexity: O(n)
    Space Complexity: O(min(n, m)), where n is the length of the string and m is the size of the character set.

    This approach is more efficient than the brute force approach, which has a time complexity of O(n^3).
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays.

    Problem Statement:
    Given two sorted arrays `arr1` and `arr2`, merge them into a single sorted array.

    Category: Two Pointers for Merging

    Algorithm Description:
    - Initialize two pointers, `i` and `j`, both starting at the beginning of `arr1` and `arr2` respectively.
    - Compare the elements at these pointers and append the smaller element to the merged array.
    - Move the pointer of the array from which the element was taken.
    - Continue this process until one of the arrays is fully traversed.
    - Append the remaining elements of the other array to the merged array.

    Time Complexity: O(n + m), where n and m are the lengths of arr1 and arr2 respectively.
    Space Complexity: O(n + m)

    This approach is more efficient than the brute force approach, which would involve concatenating the arrays and then sorting them, resulting in a time complexity of O((n + m) log(n + m)).
    """
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged


def has_cycle(head):
    """
    Detect a cycle in a linked list.

    Problem Statement:
    Given a linked list, determine if it has a cycle in it.

    Category: Fast and Slow Pointers

    Algorithm Description:
    - Initialize two pointers, `slow` and `fast`, both starting at the head of the linked list.
    - Move the `slow` pointer one step at a time and the `fast` pointer two steps at a time.
    - If there is a cycle, the `fast` pointer will eventually meet the `slow` pointer.
    - If the `fast` pointer reaches the end of the list, there is no cycle.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This approach is more efficient than the brute force approach, which would require additional space to store the visited nodes.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def find_middle(head):
    """
    Find the middle of a linked list.

    Problem Statement:
    Given a linked list, find the middle node.

    Category: Fast and Slow Pointers

    Algorithm Description:
    - Initialize two pointers, `slow` and `fast`, both starting at the head of the linked list.
    - Move the ```
    - Move the `slow` pointer one step at a time and the `fast` pointer two steps at a time.
    - When the `fast` pointer reaches the end of the list, the `slow` pointer will be at the middle node.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This approach is more efficient than the brute force approach, which would require traversing the list twice or using additional space to store the nodes.
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def detect_cycle_start(head):
    """
    Detect the start of a cycle in a linked list.

    Problem Statement:
    Given a linked list, if there is a cycle, return the node where the cycle begins. If there is no cycle, return None.

    Category: Fast and Slow Pointers

    Algorithm Description:
    - Use the fast and slow pointer technique to detect if there is a cycle.
    - If a cycle is detected, initialize another pointer at the head of the list.
    - Move both the new pointer and the slow pointer one step at a time.
    - The point at which they meet is the start of the cycle.

    Time Complexity: O(n)
    Space Complexity: O(1)

    This approach is more efficient than the brute force approach, which would require additional space to store the visited nodes.
    """
    slow, fast = head, head

    # First, determine if there is a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None  # No cycle

    # Find the start of the cycle
    start = head
    while start != slow:
        start = start.next
        slow = slow.next

    return start


import unittest

class TestTwoPointerTechniques(unittest.TestCase):

    def test_two_sum_sorted(self):
        self.assertEqual(two_sum_sorted([1, 2, 3, 4, 6], 6), (2, 4))
        self.assertEqual(two_sum_sorted([2, 3, 4, 5, 7, 8], 10), (2, 8))
        self.assertIsNone(two_sum_sorted([1, 2, 3], 7))

    def test_remove_duplicates(self):
        arr = [1, 1, 2, 2, 3, 4, 4]
        new_length = remove_duplicates(arr)
        self.assertEqual(new_length, 4)
        self.assertEqual(arr[:new_length], [1, 2, 3, 4])

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("abcd"), "dcba")
        self.assertEqual(reverse_string(""), "")

    def test_max_area(self):
        self.assertEqual(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(max_area([1, 1]), 1)
        self.assertEqual(max_area([4, 3, 2, 1, 4]), 16)

    def test_length_of_longest_substring(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([], [1, 2, 3]), [1, 2, 3])

    def test_has_cycle(self):
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None

        head = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Creates a cycle

        self.assertTrue(has_cycle(head))

        head2 = ListNode(1)
        node2 = ListNode(2)
        head2.next = node2
        self.assertFalse(has_cycle(head2))

    def test_find_middle(self):
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None

        head = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        self.assertEqual(find_middle(head).val, 3)

        head2 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        head2.next = node2
        node2.next = node3
        node3.next = node4

        self.assertEqual(find_middle(head2).val, 3)

    def test_detect_cycle_start(self):
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None

        head = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Creates a cycle

        self.assertEqual(detect_cycle_start(head).val, 2)

        head2 = ListNode(1)
        node2 = ListNode(2)
        head2.next = node2
        self.assertIsNone(detect_cycle_start(head2))

if __name__ == '__main__':
    unittest.main()
