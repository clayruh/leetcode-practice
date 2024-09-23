def majorityElement(nums):
    # initialize majority_element variable
    majority_element = nums[0]
    # initialize nums_hash 
    nums_hash = {}
    # loop through nums and create a hashmap of number : appearances
    for i in range(len(nums)):
        # if nums[i] in nums_hash:
        if nums[i] in nums_hash:
            # nums_hash[nums[i]] += 1
            nums_hash[nums[i]] += 1
            # if nums_hash[nums[i]] > nums_hash[majority_element]:
            if nums_hash[nums[i]] > nums_hash[majority_element]:
                # majority_element = nums[i]
                majority_element = nums[i]
        else:
            # initialize nums_hash[nums[i]] = 1
            nums_hash[nums[i]] = 1
    print(nums_hash)
    return majority_element

print(majorityElement([6,6,6,7,7]))