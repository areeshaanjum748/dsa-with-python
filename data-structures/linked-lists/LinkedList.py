class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self): # no need to pass head as an agrument coz intially we want the Linked List to be empty
        self.head = None
        
    def print(self):
        'Prints the Linked List'
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ('->') if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
        
    def get_length(self):
        'Returns the length of the Linked List'
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
        
    def insert_at_beginning(self, data):
        'Inserts the data at the beginning of the Linked List'
        node = Node(data, self.head)
        self.head = node
        
    def insert_at_end(self, data):
        'Inserts the data at the end of the Linked List'
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_at_index(self, index, data):
        'Inserts the data at the given index'
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
            
        if index == 0:
            self.insert_at_beginning(data)
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            
            count += 1
            itr = itr.next
            
    def remove_at_index(self, index):
        'Removes the node at the given index'
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
                
        if index == 0:
            self.head = self.head.next
            return
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
                
            count += 1
            itr = itr.next
                
    def insert_values(self, data_list):
        'Creates a Linked List with given list'
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def remove_by_value(self, data):
        'Removes the node with first occurrence of data'
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
            
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
                
            itr = itr.next
            
        
    def insert_after_value(self, data_after, data_to_insert):
        'Searchs for first occurance of data_after value in linked list'
        'Inserts data_to_insert after data_after node'
        
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.insert_at_beginning(data_to_insert)
            return
            
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    
    
ll = LinkedList()
ll.insert_at_beginning(34)
ll.insert_at_beginning(4)
ll.insert_at_end(5)
ll.insert_at_index(1, 8)
ll.remove_at_index(1)
ll.remove_by_value(89)
ll.insert_after_value(34, 45)
ll.print()
print(ll.get_length())

        
