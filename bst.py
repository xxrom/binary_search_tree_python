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


  def getMinValue(self):
    if self.root: # if root not None
      return self.getMin(self.root)

  def getMin(self, node):
    if node.leftChild: # have left Child
      getMin(node.leftChild)

    return node.data


  def getMaxValue(self):
    if self.root:
      return self.getMax(self.root)

  def getMax(self, node):
    if node.rightChild:
      getMax(node.rightChild)

    return node.data


  def traverse(self):
    if self.root:
      self.traverseInOrder(self, self.root)

  def traverseInOrder(self, node):
    if node.leftChild:
      self.traverseInOrder(node.leftChild)

    print('%s ' % node.data)

    if node.rightChild:
      self.traverseInOrder(node.rightChild)
