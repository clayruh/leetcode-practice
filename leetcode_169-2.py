def majorityElement(nums) -> int:
    # initialize dict
    nums_dict = {}
    # initialize majority_element
    majority_element = nums[0]
    # every time we loop through nums
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            nums_dict[nums[i]] += 1
        # create dictionary {num : appearances}
        # checking if dict[num] > dict[majority_element]
            # reassign majority_element
            if nums_dict[nums[i]] > nums_dict[majority_element]:
                majority_element = nums[i]
        else:
            nums_dict[nums[i]] = 1
    return majority_element

print(majorityElement([2,2,1,1,1,2,2]))