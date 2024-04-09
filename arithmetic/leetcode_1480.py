class Solution(object):
    def runningSum(self, nums):
        # function is a running sum through the array nums
        growing_sum = 0
        sums = []
        for num in nums:
            growing_sum += num
            sums.append(growing_sum)
        return sums