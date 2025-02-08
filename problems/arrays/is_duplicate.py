"""
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.
"""

# Input: nums= [1, 2, 3, 4]
# Output: false  
# Explanation: There are no duplicates in the given array.

class Solution:
    def containsDuplicate(self,nums):
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False


nums = [1, 2, 3, 4]
x = Solution()
print(x.containsDuplicate(nums))