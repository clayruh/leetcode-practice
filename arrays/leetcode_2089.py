class Solution(object):
    def targetIndices(self, nums, target):
        targetIndex = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                targetIndex.append(i)
        return targetIndex
    
    # return [ i for i in range((len(nums))) if nums[i] == target ]