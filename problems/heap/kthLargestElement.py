from typing import List
"""
Process a stream of inputs and always return the kth largest element from the values processed so far
We'll implement this using a min-heap of a fixed size k
Everytime we add a number, if the heap is already full up to k
then we instead check if the new value is larger than the min value
if so pop the min, add the new value then re-heapify which in turn will bubble
down the new kth largest value
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = MinIntHeap(capacity=k)
        for num in nums:
            self.heap.addElement(num)


    def add(self, val: int) -> int:
        return self.heap.addElement(val)


class MinIntHeap:
    def __init__(self, capacity=3):
        self.items = []
        self.size = 0
        self.capacity = capacity
        

    def getChildIndex(self,parentIndex:int,isLeft):
        if isLeft:
            return 2 * parentIndex + 1
        else:
             return 2 * parentIndex + 2
    
    def getParentIndex(self,childIndex:int):
        return(childIndex -1)//2

    def hasChild(self,index:int,isLeft:bool) -> bool:
        return self.getChildIndex(index,isLeft) < self.size
    
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
        self.items.pop(-1)
        self.heapifyDown()
        return item
            


    def addElement(self, item:int):
        if self.size == 0:
            self.items.append(item)
            self.size +=1
            return self.peek()
        else:
            if self.size == self.capacity:
                if self.items[0] < item:
                    self.popMinElement()
                else:
                    return self.peek()
            self.items.append(item)
            self.size +=1
            self.heapifyUp()
            return self.peek()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParent(index) > self.items[index]:
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
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

heapk = KthLargest(4, [4, 5, 5, 6, 6, 7])
heapk.add(3)
print(heapk.add(-2))
print(heapk.add(5))
print(heapk.add(10))
print(heapk.add(9))