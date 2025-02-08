from typing import List

class Solution:
    def merge(self, a: List[int], b: List[int]) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, c = 0, 0, []

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1

c.extend(a[i:])
c.extend(b[j:])