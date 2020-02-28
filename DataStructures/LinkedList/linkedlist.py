from node import Node

class LinkedList:

  def __init__(self,):

    self.head = None
    self.length = 0

  def add(self,data):

    self.add_node(Node(data))

  def add_node(self,node):
    if self.head is None:
      self.head = node
    else:
      tail = self._get_tail()
      tail.next = node

    self.length += 1

  def remove(self,index):
    node = self.get_node(index)
    if node is not None:
      self.remove_node(node)

  def remove_node(self,node):
    if node is self.head:
      if self.head is not None:
        self.head = self.head.next
    else:
      prev = self.head
      while prev.next is not node:
        prev = prev.next
      
      prev.next = node.next

  def _get_tail(self,):

    node = self.head
    while node.next is not None:
      node = node.next

    return node

  def get_node(self,index):
    if index < 0:
      raise ValueError('Invalid Index')
    if self.head is None or index >= self.length:
      return None
    
    node = self.head
    i = 0

    while node.next is not None and i < index:
      node = node.next
      i += 1
    
    return node
    

  def to_list(self,):
    arr = []

    node = self.head

    while node:
      arr.append(node.data)
      node = node.next
    
    return arr

  def __str__(self,):

    string = 'Linked List:\n'
    if self.head is None:
      return string

    
    node = self.head
    while node.next is not None:
      string = string + node.data + '\n'
      node = node.next

    return string + node.data

ll = LinkedList()
ll.add('Blake')
ll.add('Tyler')
ll.add('Kaya')
print(ll.to_list())