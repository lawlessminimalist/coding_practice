"""
Given an input array of nums, where nums[i] is the weight of a rock you must simulate the following
behavior:
1. Take the top two weighted rocks x,y
2. Smash them together, the outcome of which falls into these scenarios
    x = y == x and y destroyed
    x < y == x - y put backing to list
    y > x - this will never happen as x was popped first so it's either larger or a duplicate
    hence the first scenario
"""



class MaxIntHeap:
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
    
    def popMaxElement(self):
        if self.size == 0:
            raise Exception("Can't pop on an empty heap")
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
                if self.items[0] > item:
                    self.popMinElement()
                else:
                    return self.peek()
            self.items.append(item)
            self.size +=1
            self.heapifyUp()
            return self.peek()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParent(index) < self.items[index]:
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasChild(index,True):
            # find the largest child between the left and right
            largestChild = self.getChildIndex(index,True)
            # if has a right child and right is larger than left
            if self.hasChild(index,False) and self.getChild(index,False) > self.getChild(index,True):
                largestChild = self.getChildIndex(index,False)
            
            if self.items[index] > self.items[largestChild]:
                break
            else:
                self.swap(index,largestChild)
            index = largestChild



from typing import List
import math


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MaxIntHeap(capacity=math.inf)

        for stone in stones:
            heap.addElement(stone)
        
        while heap.size > 1:
            stone_x = heap.popMaxElement()
            stone_y = heap.popMaxElement()

            if stone_x == stone_y:
                continue
            if stone_x>stone_y:
                stone_z = stone_x - stone_y
                heap.addElement(stone_z)
        if heap.size == 0:
            return 0
        else:
            return heap.peek()

print(Solution().lastStoneWeight([2,2]))