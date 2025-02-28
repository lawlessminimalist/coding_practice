from typing import List
def miniMaxSum(arr:List[int]):
    arr.sort()
    min4 = arr[:-1]
    top4 = arr[1:]

    print(f"{sum(min4)} {sum(top4)}")

miniMaxSum([0,1,2,3,4])