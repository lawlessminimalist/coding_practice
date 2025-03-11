from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle edge case
        
        lookup = set(nums)  # Convert to set for O(1) lookups
        max_count = 0
        
        for num in nums:
            # Only start from the beginning of a sequence
            if num - 1 not in lookup:  
                current_num = num
                current_count = 1

                # Expand upwards
                while current_num + 1 in lookup:
                    current_num += 1
                    current_count += 1

                max_count = max(max_count, current_count)

        return max_count

# Test case
print(Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5]))  # Output: 3 (sequence: 3, 4, 5)
