"""
We will implement a heap to keep track of the kth smallest item.
Important calculations for heaps: 
    index of left of node = 2 * i + 1
    index of right of node = 
"""

class MinIntHeap:
    def __init__(self, size=0):
        self.items = []
        self.size = size

    def getChildIndex(self,parentIndex:int,isLeft):
        if isLeft:
            return 2 * parentIndex + 1
        else:
             return 2 * parentIndex + 2
    
    def getParentIndex(self,childIndex:int):
        (childIndex -1)//2

    def hasChild(self,index:int,isLeft:bool) -> bool:
        return MinIntHeap.getChildIndex(index,isLeft) < self.size
    
    def hasParent(self,index:int):
        return self.getParentIndex(index) >=0
    
    def getChild(self,index:int,isLeft:bool):
        return self.items[self.getChildIndex(index,isLeft)]
    
    def getParent(self,index:int):
        return self.items[self.getParentIndex(index)]
    
    def swap(self,idx1:int,idx2:int):
        temp = self.items[idx1]
        self.items[idx1] = self.items[idx2]
        self.items[idx2] = temp

    def peek(self):
        if self.size == 0:
            raise Exception("Can't peek an empty heap")
        return self.items[0]
    
    def popMinElement(self):
        if self.size == 0:
            raise Exception("Can't poll an empty heap")
        item = self.items[0]
        self.items[0] = self.items[self.size-1]
        self.size -=1
        self.heapifyDown()
        return item

    def addElement(self, item:int):
        if self.size == 0:
            self.items.append(item)
        else:
            self.items[self.size] = item
            self.size +=1
            self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParent(index) > self.items[index]:
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = self.size
        while self.hasChild(index,True):
            # find the smallest child between the left and right
            smallestChild = self.getChildIndex(index,True)
            # if has a right child and right is smaller than left
            if self.hasChild(index,False) and self.getChild(index,False) < self.getChild(index,True):
                smallestChild = self.getChildIndex(index,False)
            
            if self.items[index] < self.items[smallestChild]:
                break
            else:
                self.swap(index,smallestChild)
            index = smallestChild
        


x = MinIntHeap()
x.addElement(2)
x.addElement(3)
x.p