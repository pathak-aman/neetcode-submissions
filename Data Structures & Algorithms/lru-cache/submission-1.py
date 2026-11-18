class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

        self.d_head = Node(-1, -1)
        self.d_tail = Node(-1, -1)

        self.d_head.next = self.d_tail 
        self.d_tail.prev = self.d_head

    def delete_node(self, node):

        # X --- X ---d_tail    

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_node(self, node):
        temp = self.d_head.next

        node.next = temp
        temp.prev = node

        node.prev = self.d_head
        self.d_head.next = node


    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].val
            self.delete_node(self.cache[key])
            self.insert_node(self.cache[key])
            return value
        else:
            return -1     
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update in cache
            self.cache[key].val = value
            # Update in list
            self.delete_node(self.cache[key])
            self.insert_node(self.cache[key])
        else:
            if len(self.cache) >= self.capacity:
                # Remove last node
                # From list
                node_to_delete = self.d_tail.prev
                self.delete_node(node_to_delete)
                # From dict
                self.cache.pop(node_to_delete.key)
            
            # Create node
            newNode = Node(key, value)
            # Insert into cache
            self.cache[key] = newNode
            # Insert at the first of the list
            self.insert_node(newNode)