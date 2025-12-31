# Definition for a linked list node
# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def remove_duplicates(head):
    
    current, prev = head, None
    value_set = set()
    while(current):
        if current.data in value_set:
            prev.next = current.next
            current = current.next
        else:
            value_set.add(current.data)
            prev = current
            current = current.next
    
    return head
