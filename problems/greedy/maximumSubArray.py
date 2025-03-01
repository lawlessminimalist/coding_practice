def maxSumAlgo(nums):

    if len(nums) == 0 or nums == None:
        return nums
    
    maxSum = nums[0]
    currentSum = nums[0]

    for i in range(1,len(nums)):
        # is current index > currentSum?
        currentSum = max(nums[i],currentSum+nums[i])
        maxSum = max(currentSum,maxSum)
    return maxSum