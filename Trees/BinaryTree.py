
# coding: utf-8

# In[1]:


class BinaryTree(object):
    
    def __init__(self,key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
    
    def insertLeftChild(self,newNode):
        node = BinaryTree(newNode)
        if not self.leftChild:
            self.leftChild = node
        else:
            node.leftChild = self.leftChild
            self.leftChild = node
            
    def insertRightChild(self,newNode):
        node = BinaryTree(newNode)
        if not self.rightChild:
            self.rightChild = node
        else:
            node.rightChild = self.rightChild
            self.rightChild = node
    
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def getRoot(self):
        return self.key
            


# In[2]:


import math
# create binary tree of given height and data
def CreateBinaryTree(height,data):
    """DocString
    height : height of tree
    data : list of data , keys of nodes
    
    """
    nodes = math.pow(2,height)-1 # total number of nodes for given height: height: 1,2,3... excluding 0
    nodes_ = math.pow(2,height-1) # number of nodes upto level height-1
    if  len(data)-nodes_<0:
        print('expecting more elements!\nReduce height or increase data')
        return
    if len(data) > nodes:
        print('more elements received than expected! \nReduce elements or increase height')
        return
    root = BinaryTree(data.pop(0))
    queue = [root]
    h=1
    while queue and h < nodes:
        node = queue.pop(0)
        if len(data) > 0:
            leftNewNode = BinaryTree(data.pop(0))
            node.leftChild = leftNewNode
            queue.append(leftNewNode)
        if len(data) > 0:
            rightNewNode = BinaryTree(data.pop(0))
            node.rightChild = rightNewNode
            queue.append(rightNewNode)
            h +=2
    return root

