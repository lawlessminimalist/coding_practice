class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 0:
            return False
        maxReach = 0 
        localReach = nums[0]     
        for i in range(0,len(nums)):
            
            localReach = max(localReach,nums[i])
            maxReach = localReach + i

            print(f"localReach = {localReach}")
            print(f"maxReach = {maxReach}")

            if maxReach >= len(nums)-1:
                return True
            
            if localReach == 0:
                return False


            localReach -=1