"""
Given a array of strings, where each string represents an row of values - hence forming a grid
Given a pattern, determine if the pattern exists within the grid where each line of the pattern
if present in a contiguous manner

"1,[2,3],4,5"
"2,[3,4],5,6"

"2,3"
"3,4"

output = YES

"1,2,[3,4],5"
"2,[3,4],5,6"

"3,4"
"3,4"



"""


def gridSearch(G, P):
    row_idx = 0
    w_end = 0
    w_start = 0
    w_len = 1
    for row in G:
        #Check for presence of first pattern window + determine element index
        for _ in range(len(row)):
            # if first element detected build dynamic sliding window
            if row[w_start:w_end] == P[0][:w_len]:
                if row[w_start:w_end+1] == P[0]:
                    if len(P) == 1:
                         return "YES"
                    else:
                        if patternMatch(row_idx+1,w_start,P,G):
                            return "YES"
                else:
                    w_len+=1
                    w_end=w_start + w_len
            else:
                w_start = w_end
                w_end +=1
                w_len = 1
                continue
            
        row_idx +=1
        w_start = 0
        w_end = 0
    
    return "NO"

def patternMatch(row,element_index, pattern, data) -> bool:
    window_len = len(pattern[0])
    count = 1
    for idx in range(row,row + (len(pattern)-1)):
        if data[idx][element_index:element_index+window_len] == pattern[count]:
            count +=1
        else:
            return False
    return True
                

print(gridSearch(['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137'],['9505', '3845', '3530']))