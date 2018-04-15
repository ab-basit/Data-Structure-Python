
# coding: utf-8

# In[1]:


class BinarySearchTree(object):
    
    def __init__(self,data = None,leftChild = None,rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild


# In[2]:


def CreateBST(datalist):
    #datalist = list(set(datalist))  #  first elt is root but set will sort it
    root = BinarySearchTree(datalist.pop(0))    
    while len(datalist) != 0:
        auxRoot = root
        nodeData = datalist.pop(0)
        node = BinarySearchTree(nodeData) 
        while auxRoot:
            if nodeData == auxRoot.data:
                break
            if nodeData < auxRoot.data:
                if not auxRoot.leftChild:
                    auxRoot.leftChild = node
                    break
                else:
                    auxRoot = auxRoot.leftChild
            else:
                if not auxRoot.rightChild:
                    auxRoot.rightChild = node
                    break
                else:
                    auxRoot = auxRoot.rightChild
    return root


# In[3]:


def inOrder(root):
    if not root:
        return
    inOrder(root.leftChild)
    print(root.data,end='\n')
    inOrder(root.rightChild)

