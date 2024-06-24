class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
# initialize dictionary
        nums_dict = {}
# for loop thru nums
        for num in nums:
# check dict for num. if num is in dict, that means the counter is now 2, so return True!
            if num in nums_dict:
                return True
# if num is not in dict, then add it in
            nums_dict[num] = 1
# if everything in this loop doesn't qualify, return False
        return False