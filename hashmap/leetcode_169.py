def majorityElement(nums) -> int:
    # could sort nums so numbers are grouped together but sorting is O(n log(n)) time
    nums.sort()
    nums_dict = {}
    # create a dictionary to count number:appearances and then loop through dict to find the biggest # of appearances
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else: 
            nums_dict[num] = 1
    print(nums_dict)
    
    most_seen = 0
    majority_element = 0
    for num in nums_dict:
        if nums_dict[num] > most_seen:
            most_seen = nums_dict[num]
            majority_element = num
    # print(majority_element, most_seen)
    return majority_element

print(majorityElement([3,3,4]))