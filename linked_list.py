class Node(object):
    def __init__(self, data, next=None, prev=None):
        """ Initialize a new node with the given data """
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        """ Initialize this linked list. """
        self.head = None
        self.tail = None

    def append(self, item):
        """ A method to add an item to the end of the linked list """
        new_node = Node(item)
        if self.head == None:  # Check if the linkedlist is empty
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def prepend(self, item):
        """ A method to add an item to the beginning of the list """
        new_node = Node(item)
        if self.head == None:  # Check if the linkedlist is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_songs(self):
        """ A method to print out all the songs in your playlist """
        if self.head == None:
            print("The playlist is empty!")
        else:
            current_node = self.head
            while current_node:
                print(current_node.data)
                current_node = current_node.next

    def delete_from_head(self):
        """ A method to delete an item from the beginning of the linked list """
        if self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            print("The playlist is empty!")

    def delete_from_tail(self):
        """ A method to delete an item from the end of the linked list """
        if self.head:  # Check if the linkedlist is empty
            if self.head == self.tail:  # If there is only one node in the list
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                previous_node = None
                while current_node.next != None:
                    previous_node = current_node
                    current_node = current_node.next
                current_node.prev = None
                previous_node.next = None
                self.tail = previous_node
        else:
            print("The playlist is empty!")

    def find(self, item):
        """ A method that takes in one parameter item and returns True if found and False if not """
        current_node = self.head
        isFound = False
        while current_node and isFound == False:
            if current_node.data == item:
                isFound = True
            current_node = current_node.next
        return isFound

    def reverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev
