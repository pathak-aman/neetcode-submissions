"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        old_to_new_dict = {}

        print(node)

        if node is None:
            return node

        def copy(node):
            if node is None or node in visited:
                return
            
            visited.add(node)
            old_to_new_dict[node] = Node(node.val)
            for neighbor in node.neighbors:
                copy(neighbor)

        
        def connect(node, old_to_new_dict):
            for old_node, new_node in old_to_new_dict.items():
                for old_neighbor in old_node.neighbors:
                    new_neighbor = old_to_new_dict[old_neighbor]
                    new_node.neighbors.append(new_neighbor)

        copy(node)
        connect(node, old_to_new_dict)
        return old_to_new_dict[node] 


