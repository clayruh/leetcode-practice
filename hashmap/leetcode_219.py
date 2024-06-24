def containsNearbyDuplicate(nums, k):
    nums_dict = {}
    # maybe using a dictionary where num:i, so we're tracking index and number

    # iterate through nums
    # if nums[i] is already a key in nums_dict dict, 
    # second_index = i, first_index = nums_dict.get("num")
    # then run if abs(first_index - second_index) <=k, return True
    # but if the numbers are the same and the k isn't true, then update the dict and keep going 

    # updating the dict is the way to go here!

    # nums_dict[nums[i]] = i
    
    # else return False
    
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            index_j = i
            index_i = nums_dict.get(nums[i])
            if (abs(index_i - index_j) <= k):
                return True
            else: 
                nums_dict.update({nums[i] : i})
        else:
            nums_dict[nums[i]] = i
    return False

containsNearbyDuplicate([1,2,3,1,2,3], 2)