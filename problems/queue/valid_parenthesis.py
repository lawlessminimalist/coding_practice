class Solution:
    def isValid(self, s: str) -> bool:
        openers = set(['(', '{', '[' ])
        closers = set([')', '}', ']'])
        opening_pair = {'(':')','{':'}','[':']'}
        seen = []
        for bracket in s:
            if bracket in openers:
                seen.append(bracket)
            else:
                if len(seen) == 0:
                    return False
                if bracket != opening_pair[seen[-1]]:
                    return False
                else:
                    seen.pop()
        if len(seen) > 0:
            return False
        return True

print(Solution().isValid('({[[[]]]})[]]{()}'))