class Solution:
    @staticmethod
    def isBadVersion(n):
        if n >= 6:  # All versions from 3 onwards are bad
            return True
        return False
    
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Working with version numbers directly
        
        while left < right:
            middle = left + (right - left) // 2  # Avoid potential overflow
            
            if self.isBadVersion(middle):
                right = middle  # Move left since we need the FIRST bad version
            else:
                left = middle + 1  # Move right to find the first bad version
        
        return left  # Left will be the first bad version

# Test
x = Solution()
print(x.firstBadVersion(10))  # Output should be 3
