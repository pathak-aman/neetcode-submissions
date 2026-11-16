"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new_map = {None: None}

        # Pass 1: Create nodes with same value
        curr = head
        while curr:
            new_node = Node(curr.val)
            old_new_map[curr] = new_node
            curr = curr.next
        
        # Pass 2: Assign pointers
        curr = head
        while curr:
            old_next_node = curr.next
            old_random_node = curr.random

            new_node = old_new_map[curr]

            new_node.next = old_new_map[old_next_node]
            new_node.random = old_new_map[old_random_node]

            curr = curr.next
        return old_new_map[head]

