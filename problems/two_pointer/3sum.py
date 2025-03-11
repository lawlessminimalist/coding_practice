from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []
        count1 = 0
        seen = set()
        for num1 in nums:
            count2 = 0
            if count1 in seen:
                continue
            for num2 in nums:
                count3 = 0
                if count2 in seen:
                    continue
                for num3 in nums:
                    if count3 in seen:
                        continue
                    value = num1 + num2 + num3
                    print(f"{num1},{num2},{num3} = {value}")
                    if value == 0:
                        triplets.append([num1,num2,num3])
                        seen.add(count1)
                        seen.add(count2)
                        seen.add(count3)
                    count3+=1
                count2+=1
            count1+=1
        return triplets
                    
print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))
