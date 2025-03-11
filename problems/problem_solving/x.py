"""
String, find the length of the longest substring without repeating characters

Input
abcabbc

Output
abca[bb]c

"""


def repeatingChars(s):
    if not s:
        return 0  # Handle empty string case

    longest = 1  # At minimum, a single character is a repeating sequence
    left = 0

    for right in range(1, len(s)):
        if s[right] == s[right - 1]:  
            longest = max(longest, right - left + 1)  
        else:
            left = right  # Reset the window when a different character appears

    return longest

print(repeatingChars("aaabbccddddee"))
