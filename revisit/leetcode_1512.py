def numIdenticalPairs(nums):
    good_pairs = 0
    # map each number to an index into a dictionary {num : [indexes where the num shows up in nums]}
        # {1:[0, 3, 4], 3:[2, 5]}
        # {1:[0, 1, 2, 3]}
    # then a for loop through the dictionary or nums
    # if the length of the array at the value is > 1,
    # do something lol
    dict = {}

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = [i]
        else:
            dict[nums[i]].append(i)
    print(dict)

    for key in dict:
        if len(dict[key]) > 1:
            arr = dict[key]
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    good_pairs += 1
    return good_pairs
        
print(numIdenticalPairs([1,2,3]))