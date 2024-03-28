class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # say candies = [2,3,5,1,3] extraCandies = 3
        # output: [true,true,true,false,true]
        result = []
        maxCandies = max(candies)
        # for loop through `len(candies)`
        for i in range(len(candies)):
        # if candies[i] += extraCandies is greater than `max(candies)`, return `true`
            if (candies[i] + extraCandies) >= maxCandies:
                result.append(True)
        # if candies[i] += extraCandies is less than or equal to `max(candies)`, return `false`
            else:
                result.append(False)
        # add/append the return to array `result`
        return result
    
    # that was kind of a struggle.. using just `for i in candies` didn't seem to work. I kept getting index out of range errors, so changed to `for i in range(len(candies)):`