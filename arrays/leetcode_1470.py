def shuffle(nums, n):
    # n represents the index where the nums[n] should start to be inserted

    # initiate a new array
    shuffled_arr = []
    # for loop through nums
    for i in range(n):
    # while looping, append nums[i] then numx[n]
        shuffled_arr.append(nums[i])
        shuffled_arr.append(nums[n])
        n += 1
    # return new array
    return shuffled_arr

print(shuffle([1,1,2,2], 2))
        