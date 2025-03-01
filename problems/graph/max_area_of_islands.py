from typing import List
from collections import deque

"""
Given a matrix of 0's and 1's where:
0 = water
1 = land
return the number of island masses, of which an island is a connnect mass
in the matrix of connected (up,down,left,right) land points.

Use BFS to scan the connected grid upon detecting the start of an island
whilst iterating through the grid. Keep track of visited nodes and skip those
after detecting the end of the land mass.

"""

class Solution:

    def bfs(self,area:int,queue:deque, seen:set,node:tuple[int,int],grid:List[List[str]]):

        if grid[node[0]][node[1]] == 0:
            return area
        area +=1

        left,right,up,down = (node[0]-1,node[1]),(node[0]+1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)
        for item in [left,right,up,down]:
            if item[0] < len(grid) and item[0] >=0:
                if item[1] < len(grid[0]) and item[1] >= 0:
                    if grid[item[0]][item[1]] == 1 and item not in seen:
                        queue.append(item)
                        seen.add(item)
        while queue:
            new_node = queue.popleft()
            area = self.bfs(area,queue,seen,new_node,grid)
        
        return area
    
    def dfs(self,area,seen,node,grid):
        
        if grid[node[0]][node[1]] == 0:
            return
        
        area+=1
    
        left,right,up,down = (node[0]-1,node[1]),(node[0]+1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)
        for item in [left,right,up,down]:
            if item[0] < len(grid) and item[0] >=0:
                if item[1] < len(grid[0]) and item[1] >= 0:
                    if grid[item[0]][item[1]] == 1 and item not in seen:
                        seen.add(item)
                        area = self.dfs(area,seen,item,grid)
        
        return area


    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        seen = set()
        max_area = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1 and (row,column) not in seen:
                    seen.add((row,column))
                    max_area = max(max_area,self.dfs(0,seen,(row,column),grid))
        return max_area
    
print(Solution().maxAreaOfIsland(
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]
))