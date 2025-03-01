from typing import List

def search(arrs:List[int],target:int):
    left,right = 0, len(arrs) -1

    while left <= right:
        mid = (left + right )//2

        if arrs[mid] == target:
            return mid
        
        if arrs[mid] < target: 
            left = mid + 1

        if arrs[mid] > target:
            right = mid - 1

    return -1

print(search([0,1,2,3,5,7,777,12222],-111))
