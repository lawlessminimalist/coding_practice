#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#

def getRemovableIndices(str1, str2):
    # Write your code here
    countStr1 = collections.Counter(str1)
    countStr2 = collections.Counter(str2)
    count_swaps = 0
    for key in countStr1.keys():
        if countStr1[key] > countStr2[key]:
            target_char = key
            count_swaps+=1
    if count_swaps > 1:
        return [-1]
    p1 = 0
    p2 = 0
    removableIndicies = []
    while (p1 < len(str1) and p2<len(str2)):
        charStr1 = str1[p1]
        charStr2 = str2[p2]
        if charStr1 == target_char:
            if charStr2 == target_char:
                if validation_func(str1,str2,p1):
                    removableIndicies.append(p1)
                    p1+=1
                    continue
        p1+=1
        p2+=1
    return removableIndicies

def validation_func(str1:str,str2:str,idx:int):
  front = str1[:idx]   # up to but not including n
  back = str1[idx:]  # n+1 through end of string
  if front + back == str2:
      return True
  else:
      return False



    
print(getRemovableIndices('aabbb','aabb'))
