class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0  # max frequency of a single char in the current window
        left = 0
        result = 0
        
        for right in range(len(s)):
            # Update the count of the current char at the right of the window
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            
            # current window length is right - left + 1
            # if the number of characters to replace (window length - max_count) > k, shrink window
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result

Solution().characterReplacement("AABABB",1)