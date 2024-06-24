def containsNearbyDuplicate(nums, k) -> bool:
# using a dictionary to relate number to index 
# want to relate an num's index to the num, so dictionary! and not just floating variables

# initiate a dict to store nums + index relationships
    nums_dict = {}
# loop thru nums
    for i in range(len(nums)):
# assuming num is in dict, use the existing index and check the second condition of abs(i-j) <= k and return True
        if nums[i] in nums_dict:
            if abs(i - nums_dict[nums[i]]) <= k:
                return True
# if num isn't in the dict, add it to the dict/updating the index
        nums_dict[nums[i]] = i
# after the entire loop if nothing has been qualified, return False
    return False