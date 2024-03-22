class Solution(object):
    def findGCD(self, nums):
        # loop thru nums, find smallest + largest numbers
        # set variables to first number in the array, so that when we can compare
        print("starting function")
        smallNum = nums[0]
        bigNum = nums[0]
        for i in nums:
        # variable to store smallest num smallNum
        # compare smallNum to current number (i)
            smallNum = min(smallNum, i)
            bigNum = max(bigNum, i)
            # if smallNum > i:
            #     smallNum = i
            # if bigNum < i:
            #     bigNum = i
        # variable to store biggest num bigNum
        # compare bigNum to current number (i)
        print("smallNum:", smallNum, "bigNum:", bigNum)
        # return greatest common divisor of smallNum and bigNum
        # if bigNum%smallNum == 0:
        #     return smallNum
        # # while bigNum%n != 0 && smallNum%n != 0 
        # n = smallNum - 1
        n = smallNum
        print(n, smallNum)
        while bigNum%n != 0 or smallNum%n != 0:
            n -= 1
        return n

print(findGCD([30,60]))

nums = [4,9,9,10]
nums = [31, 60]