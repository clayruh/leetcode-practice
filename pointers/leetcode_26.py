def removeDuplicates(nums) -> int:
    # use a set to track nums seen
    nums_seen = set()
    # initiate variable index for number's new index
    new_index = 0
    # loop through nums
    for num in nums:
    # if num not in set, add to set and update the index += 1
        if num not in nums_seen:
            nums_seen.add(num)
            nums[new_index] = num
            new_index += 1
    return new_index

print(removeDuplicates([1,1,2]))