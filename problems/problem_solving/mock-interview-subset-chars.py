"""
find the maximum number of substrings in superset when superset contains wildcards
input = superset = "a??gz?b?" subset = "ab" 
output = 3

"""

from collections import Counter

def findMaxSubstrings(superset, subset):

    # Edge cases
    if len(subset) == 0 or len(subset)>len(superset):
        return 0
    
    # Get count of complete substrings
    count = superset.count(subset)
    # Remove all occurrences of the substring.
    replaced_string = superset.replace(subset, "")

    wild_card_count = superset.count('?')

    





