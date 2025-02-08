import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        s = ''.join(char for char in s if char.isalnum())

        # double pointer problem - find the centre of a string and compare [len(s)/2-i] with [len(s)/2+i]
        center = math.ceil((len(s)/2)-1)
        p1 = center
        p2_start = center if len(s) % 2 != 0 else center + 1
        for p2 in range(p2_start,len(s)):
            if s[p1] != s[p2]:
                return False
            p1=p1-1
        return True
    
print(Solution().isPalindrome(s="Madam, in Eden, I'm Adam"))

        