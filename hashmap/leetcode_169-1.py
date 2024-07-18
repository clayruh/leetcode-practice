def majorityElement(nums) -> int:
    # initiate a max_appearances
    # initiate max_element
    max_appearances = 0
    max_element = 0
    nums_dict = {}
    # loop through nums
    for num in nums:
        if num in nums_dict:
    # set number:appearances
            nums_dict[num] += 1
    # if number of appearances is the greatest we've seen, re-set max_appearances and max_element
            if nums_dict[num] > max_appearances:
                max_appearances = nums_dict[num]
                max_element = num
    # else initiate with num : 1
        else:
            nums_dict[num] = 1
            # adding repetitive logic for edge case nums = [1]
            if nums_dict[num] > max_appearances:
                max_appearances = nums_dict[num]
                max_element = num
    return max_element

print(majorityElement([1]))
# run time is O(n) to create the dict