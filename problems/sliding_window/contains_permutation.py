class Solution:
    """
    Example of a simple static sliding window issue in which we need to find the occurance of a substring.
    The ordering of the chars in the substring can be sorted in order to do a char level inclusion check
    """
    """Naive
    O(n * m log m)
    The sort is expensive on the sub-array - we can instead do this in O(n) time by calculating freq and updating
    per iteration/slide operation
    """
    def checkInclusionNaive(self, s1: str, s2: str) -> bool:
        left = 0
        destructured_str = list(s1)
        destructured_str.sort()
        for right in range(len(s1),len(s2)+1):
            window = list(s2[left:right])
            window.sort()
            if window == destructured_str:
                return True
            else:
                left +=1
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0

        comp_freq = self.calculateFreq(s1)
        window_size = len(s1)

        window_freq = []
        for right in range(window_size-1,len(s2)):
            if right == window_size-1:
                init_window = s2[left:window_size]
                window_freq = self.calculateFreq(init_window)
                if window_freq == comp_freq:
                    return True
                else:
                    pos = ord(s2[left]) - ord('a')
                    window_freq[pos] = window_freq[pos] -1
                    left +=1
            else:
                pos = ord(s2[right]) - ord('a')
                window_freq[pos] = window_freq[pos]+1
                if window_freq == comp_freq:
                    return True
                else:
                    pos = ord(s2[left]) - ord('a')
                    window_freq[pos] = window_freq[pos] -1

                    left +=1
        return False
                

    def calculateFreq(self,string:str) -> list[int]:
        count = [0] * 26
        for char in range(len(string)):
            count[ord(string[char]) - ord('a')] += 1
        return count

print(Solution().checkInclusion("abc","asbcaflkjanf"))