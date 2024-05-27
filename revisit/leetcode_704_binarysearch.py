def search(nums, target):

    l_index = 0
    r_index = len(nums) - 1
    result = -1

    while l_index <= r_index:
        # add the boundary indexes and then divide by 2
        midpoint = (l_index + r_index)// 2
        if nums[midpoint] <= target:
            l_index = midpoint + 1
            result = midpoint
        else:
            r_index = midpoint - 1
    if nums[result] != target:
        result = -1
    return result