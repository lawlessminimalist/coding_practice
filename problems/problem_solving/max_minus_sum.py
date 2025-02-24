from typing import List
import math 
def miniMaxSum(arr:List[int]):
    arr.sort()
    min4 = arr[:-1]
    top4 = arr[1:]

    print(sum(min4))
    print(sum(top4))

miniMaxSum([0,1,2,3,4])