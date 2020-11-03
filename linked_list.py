class Node(object):
  def __init__(self,data):
    """ Initialize a new node with the given data """
    self.data = data
    self.next = None

class  LinkedList(object):
  def __init__(self):
    """ Initialize this linked list. """
    self.head = None
    self.tail = None
  def append(self,item):
    """ A method to add an item to the end of the linked list """
    new_node = Node(item)
    if !self.head: # Check if the linkedlist is empty
      self.head = new_node
    else:
      self.tail.next = new_node
    self.tail = new_node
  def prepend(self,item):
    """ A method to add an item to the beginning of the list """
    new_node = Node(item)
    if !self.head: # Check if the linkedlist is empty
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node