
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import List, Optional

class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return node
        
        seen:dict[Node:Node] = {}
        clonedNode = Node(node.val,[])
        seen.update({node:clonedNode})
        seen[node].neighbors += [self.recurseNeighbors(neighbor,seen) for neighbor in node.neighbors]
        return seen[node]


    def recurseNeighbors(self,node: Optional['Node'],seen:dict):
        if node in seen:
            return seen[node]
        else:
            seen.update({node:Node(node.val,[])})
            seen[node].neighbors += [self.recurseNeighbors(neighbor,seen) for neighbor in node.neighbors]
        return seen[node]






node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Set up neighbors (edges) to form the graph:
# node1 is connected to node2
# node2 is connected to node1 and node3
# node3 is connected to node2

node1.neighbors = [node2]
node2.neighbors = [node1,node3]
node3.neighbors = [node2]

Solution().cloneGraph(node1)

