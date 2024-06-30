def twoSum(nums, target):
    # nums is an array, target is the sum of two numbers in nums
    # return indices of the two nums that add up to target

    # I spent so long down the wrong rabbit hole
    # SO what we want to do, is create a dictionary of 
    #   target - last value : tracked indices
    #   aka ... if nums = [2,7,11,15] target = 9
    #   dict = { 7:0, 2:1, -2:2, -6:3 }
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            return [i, nums_dict[nums[i]]]
        else:
            nums_dict[target - nums[i]] = i

twoSum([2,7,11,15], 9)