class Node(object):

  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

class BinarySearchTree(object):

  def __init__(self):
    self.root = None

  def insert(self, data):
    if not self.root:
      self.root = Node(data)
    else:
      self.insertNode(data, self.root);

  # O(LogN) !!! if we have balanced tree else it can be O(N)
  # --> AVL RBT are needed for balancing !!!
  def insertNode(self, data, node):
    if data < node.data: # основное правило, left < root < right !!!
      if node.leftChild: # if left not None => insert in left sub tree
        self.insertNode(data, node.leftChild)
      else:
        node.leftChild = Node(data)
    else: # data >= node.data:
      if node.rightChild: # if left not None => insert in right subtree
        self.insertNode(data, node.rightChild)
      else:
        node.rightChild = Node(data)
