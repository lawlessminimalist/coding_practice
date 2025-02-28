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

    def bfs(self,seen:set,node:tuple[int,int],grid:List[List[str]]):
        seen.add(node)
        queue = deque()

        if grid[node[0]][node[1]] == '0':
            return

        left,right,up,down = (node[0]-1,node[1]),(node[0]+1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)
        for item in [left,right,up,down]:
            if item[0] < len(grid) and item[0] >=0:
                if item[1] < len(grid[0]) and item[1] >= 0:
                    if grid[item[0]][item[1]] == '1' and item not in seen:
                        queue.append(item)
        while queue:
            self.bfs(seen,queue.popleft(),grid)


    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1' and (row,column) not in seen:
                    self.bfs(seen,(row,column),grid)
                    islands +=1
        return islands
    
print(Solution().numIslands([["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]))