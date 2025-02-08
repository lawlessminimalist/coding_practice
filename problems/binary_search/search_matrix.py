from typing import List

"""
Given a 2D matrix that's both sorted at the column and row level, find a target value
with a solution that operates in O(log(n*m)) time and O(1) space complexity. This lends
itself to binary search both within the array and across the column level.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix) == 1:
            return Solution.searchRow(matrix[0],target)
        else:
            row = Solution.searchColumn(matrix,target)
            if not row:
                return False
            return Solution.searchRow(row,target)

    """ 
    Function to search at the column level to identify which
    row contains the value. Accepts the original column input.
    """
    @staticmethod
    def searchColumn(arr: List[List[int]],target:int) -> List[int]:
        # Base case
        down,up = 0,len(arr)-1
        while down<=up:
            mid = (down+up)//2
            
            ## check if middle row contains value by checking range
            if arr[mid][0] <= target <= arr[mid][-1]:
                return arr[mid]
            
            ## if start of array is higher than target, too far up in search space

            if arr[mid][0] >= target:
                up = mid - 1
            else:
                down = mid +1

        return False
    
    @staticmethod
    def searchRow(arr:List[int],target:int) -> bool:
        left,right = 0,len(arr)-1
        while left<=right:
            mid = (left + right)//2

            if arr[mid] == target:
                return True

            if arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return False 
    
matrix=[[1],[3]]
target=0

print(Solution().searchMatrix(matrix,target))