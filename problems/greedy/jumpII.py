"""

Given this is a greedy solution, lets think about what the sub-problem is
We're trying to minimize the amount of jumps to reach the end
Assuming that there is a solution
We could move backwards through the array, looking for the 

"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        numJumps = 0
        count = 0
        localReach = nums[count]

        while count <= len(nums)-1:

            localMax = -1
            localMaxIndex = 0

            if count + localReach >= len(nums)-1:
                return numJumps+1
            
            for localIndex in range(count+1,count+(localReach+1)):
                if localIndex > len(nums):
                    return numJumps + 1
                
                if nums[localIndex] > localMax:
                    localMax = nums[localIndex]
                    localMaxIndex = localIndex
                if nums[localIndex] == localMax:
                    localMaxIndex = localIndex

            numJumps += 1
            count = localMaxIndex
            localReach = localMax
        return numJumps


print(Solution().jump(nums=[1,1,1,1,1]))