class Node(object):

  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

class BinarySearchTree(object):

  def __init__(self):
    self.root = None


  # O(logN) or O(N)
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
    else:
      self.insertNode(data, self.root);
  ###
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


    # O(logN)
  def remove(self, data):
    if self.root:
      self.root = self.removeNode(data, self.root)
  ###
  def removeNode(self, data, node):
    if node == None: # if node None ??? разве обязательно нужно ???
      return node # нужно для установки у родителя None

    if data < node.data: # в левом поддереве ищем
      node.leftChild = self.removeNode(data, node.leftChild)
    elif data > node.data: # в правом поддереве ищем
      node.rightChild = self.removeNode(data, node.rightChild)
    else: # нашли node

      if not node.leftChild and not node.rightChild: # 1 случай - лист
        print('[1] Remove a leaf node ... %s ' % data)
        del node
        return None

      if not node.leftChild or not node.rightChild: # 2 случай - один ребенок
        print('[2] Remove parent with one child ... %s ' % data)

        tempNode = node.rightChild
        if node.leftChild:
          tempNode = node.leftChild

        del node # удаляем найденный node
        return tempNode # возвращаем вместо удаленного - сохраненный

      # 3 случай - два ребенка
      #  I  - в правом ищем MIN node (либо в левом MAX), меняем его
      #  II - вызываем удаление с найденным MIN node (либо MAX)
      print('[3] Remove parent with two childs ... %s ' % data)
      minNode = self.getMinNode(node.rightChild) # нашли
      print('minNode %s ' % minNode.data)
      node.data = minNode.data # меняю значения на MIN в правом
      node.rightChild = self.removeNode(minNode.data, node.rightChild) # удаляю в правом MIN значение

    return node
  ###
  def getMinNode(self, node): # находим MIN node в дереве
    if node.leftChild:
      return self.getMinNode(node.leftChild)

    return node


  # O(logN)
  def getMinValue(self):
    if self.root: # if root not None
      return self.getMin(self.root)
  ###
  def getMin(self, node):
    if node.leftChild: # have left Child
      return self.getMin(node.leftChild)

    return node.data # if leftChild None => return data


  # O(logN)
  def getMaxValue(self):
    if self.root:
      return self.getMax(self.root)
  ###
  def getMax(self, node):
    if node.rightChild:
      return self.getMax(node.rightChild)

    return node.data # id rightChil`d None => return data


  # O(N)
  def traverse(self):
    print('traverse %s ' % self.root.data)
    if self.root:
      self.traverseInOrder(self.root)
  ###
  def traverseInOrder(self, node): # выводим по возрастанию
    # идем в самую левую и глубокую часть дереве и потом рекурсией
    # начинаем подниматься по дереву обратно
    if node.leftChild:
      self.traverseInOrder(node.leftChild)

    print('%s ' % node.data) # выводим корень, у которого нет левого ребенка

    if node.rightChild:
      self.traverseInOrder(node.rightChild)


# проверяем на нахождение MIN и MAX и вывод дерева
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15.5)
bst.insert(6)

print(' MIN = %s ' % bst.getMinValue())
print(' MAX = %f ' % bst.getMaxValue())
bst.traverse()

# проверяем на string значения и вывод
bst2 = BinarySearchTree() # we can pass not only numbers =)
bst2.insert('C')
bst2.insert('B')
bst2.insert('G')
bst2.insert('Z')
bst2.traverse()


# проверяем на удаление элемента 1, 2 и 3 случаи
bst3 = BinarySearchTree()
bst3.insert(32)
bst3.insert(10)
bst3.insert(55)
bst3.insert(79)
bst3.insert(1)
bst3.insert(19)
bst3.insert(16)
bst3.insert(23)

bst3.traverse()
print('  remove 10')
bst3.remove(10)
bst3.traverse()
print('  remove 1')
bst3.remove(1)
bst3.traverse()
print('  remove 55')
bst3.remove(55)
bst3.traverse()
