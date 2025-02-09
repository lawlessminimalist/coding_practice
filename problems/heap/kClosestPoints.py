


class MinHeap:
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
            


    def addElement(self, item):
        if self.size == 0:
            self.items.append(item)
            self.size +=1
            return self.peek()
        else:
            if self.size == self.capacity:
                if self.items[0][1] < item[1]:
                    self.popMinElement()
                else:
                    return self.peek()
            self.items.append(item)
            self.size +=1
            self.heapifyUp()
            return self.peek()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParent(index)[1]  > self.items[index][1]:
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasChild(index,True):
            # find the smallest child between the left and right
            smallestChild = self.getChildIndex(index,True)
            # if has a right child and right is smaller than left
            if self.hasChild(index,False) and self.getChild(index,False)[1] < self.getChild(index,True)[1] :
                smallestChild = self.getChildIndex(index,False)
            
            if self.items[index][1]  < self.items[smallestChild][1] :
                break
            else:
                self.swap(index,smallestChild)
            index = smallestChild



import math
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = MinHeap(capacity=math.inf)
        for idx in range(len(points)):
            heap.addElement((idx,Solution.calcDistance(points[idx])))
        
        result = []
        for i in range(k):
            result_idx = heap.popMinElement()[0]
            result.append(points[result_idx])
        return result


    """
    Calculate the eucledian distance between two points, x,y from the coordinate of 0,0
    using this formula (sqrt((x1 - x2)^2 + (y1 - y2)^2))
    """
    @staticmethod
    def calcDistance(coordinate:List[int]):
        x1,y1 = 0,0
        x2,y2 = coordinate[0],coordinate[1]
        return (math.sqrt((x1-x2)**2 + (y1 -y2)**2))
    
print(Solution().kClosest(points = [[0,2],[2,2]], k = 1))