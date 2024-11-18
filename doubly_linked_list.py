# Noah Preston , CSC-231-001

class Node: # Initialize Node class
    def __init__(self, data):
        self.data = data # Store data 
        self.next = None # Pointer to next node in list
        self.prev = None # Pointer to previous node in list

    def __str__(self): # Return string of data
        return str(self.data)


class DoublyLinkedList: # Inititalize DoublyLinkedList class
    def __init__(self):
        self.head = None # Pointer to first node in list
        self.tail = None # Pointer to last node in list
        self.size = 0 # Size of list, set to 0

    def is_empty(self): # Returns True if list is empty
        return self.size == 0

    def add(self, item): # Add an item 
        new_node = Node(item) # Create a new node 
        if self.is_empty(): # Checks if list is empty
            self.head = new_node # If empty, creates new head node
            self.tail = new_node # If empty, creates new tail node
        else: # Otherwise if the list is not empty 
            new_node.next = self.head # Link new node's next to current head 
            self.head.prev = new_node # Link current head's previous node to new node 
            self.head = new_node # Update head to new node
        self.size += 1 # Increment the size of the list 

    def append(self, item): # Appending an item
        new_node = Node(item) # Create a new node
        if self.is_empty(): # Checks if list is empty
            self.head = new_node # If empty, creates new head node 
            self.tail = new_node # If empty, creates new tail node
        else: # Otherwise if list is not empty
            new_node.prev =  self.tail # Link new node's previous to current tail
            self.tail.next = new_node # Link curent tail's next to new node
            self.tail = new_node # Update tail to new node
        self.size += 1 # Increment the size of the list

    def pop(self, pos = None): # Remove and return node by popping
        if self.is_empty(): # If list is empty, raise an error
            raise IndexError("Pop from an empty list.")

        if pos is None: # If no position is given, pop the last node 
            pos = self.size - 1  # Go to last position

        if pos < 0 or pos >= self.size: # Check if the position is in a valid range or raise error
            raise IndexError("Position out of range.")

        if pos == 0:  # Removing the head
            data = self.head.data # Store data of the head node
            self.head = self.head.next # Set the head to the next node
            if self.head: # If new head, update pointer
                self.head.prev = None
            else: # If list is empty, set the tail to None
                self.tail = None  
        elif pos == self.size - 1:  # Removing the tail
            data = self.tail.data # Store data of the tail node
            self.tail = self.tail.prev # Set the tail to the previous node
            if self.tail: # If new tail, update pointer
                self.tail.next = None
            else: # If list is empty, set the head to None
                self.head = None  # List is now empty
        else:  # Removing the middle
            current = self.head # Start at head node
            for _ in range(pos): # Traverse through list to the node
                current = current.next 
            data = current.data # Store the data of the current node
            current.prev.next = current.next # Link previous node to next node
            current.next.prev = current.prev # Link next node to previous node
        self.size -= 1 # Deincrement the size of the list
        return data # Return the removed node

    def search(self, item): # Search the list 
        current = self.head # Start at head node
        while current: # Traverse through list using a while loop
            if current.data == item: # If the current node matches the item being searched for then return True 
                return True
            current = current.next # Move to next node
        return False # Return False if utem being searched for is not found

    def remove(self, item): # Remove node from list
        if self.is_empty(): # If list is empty, raise error
            raise ValueError("List is empty.")

        current = self.head # Start at head node
        while current: # Traverse through list with while loop
            if current.data == item: # Checks if current node equals item being searched for 
                if current.prev: # If current node has a previous node
                    current.prev.next = current.next # Link previous node to the next node 
                if current.next: # If current node has a 
                    current.next.prev = current.prev
                if current == self.head:  # Update head
                    self.head = current.next
                if current == self.tail:  # Update tail 
                    self.tail = current.prev
                self.size -= 1 # Decrease siz of list
                return  
            current = current.next 
        raise ValueError(f"Item {item} not found in list.")
    
    def __len__(self):
        return self.size

    def __iter__(self): # Iterator to loop over list
        current = self.head
        while current:
            yield current
            current = current.next
