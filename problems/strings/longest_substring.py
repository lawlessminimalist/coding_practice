"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        p1 = 0
        p2 = 0
        count = 0
        longest = 0

        while p2 < len(s):
            # detect start and add first seen
            if p2 == 0:
                seen.add(s[p2])
                p2 +=1
                count +=1
            # duplicate detection behaviour
            elif s[p2] in seen:
                seen.remove(s[p1])
                count -=1
                p1+=1
            else:
                seen.add(s[p2])
                count +=1
                p2 +=1
            if count > longest:
                longest = count
        return longest
            


print(Solution().lengthOfLongestSubstring("abcabcbb"))