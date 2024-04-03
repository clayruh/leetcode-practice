class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # jewels is a string representing jewels
        # stones is also a string
        # trying to find how many letters in stones match jewels (case sensitive)
        searchableJewels = [ jewel for jewel in jewels ]
        howManyJewels = 0

        for stone in stones:
            if stone in searchableJewels:
                howManyJewels += 1

        # variable to track # of jewels in stones
        # split up `jewels` into singular letters? 'cause we don't want to check the whole string, just bits of it against `stones`
        return howManyJewels
    
