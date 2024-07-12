def minimumOperations(nums):
    # counter = 0
    # for loop through nums (num + 1)%3 == 0 or (num - 1)%3 == 0:
    # counter += 1
    counter = 0
    for num in nums:
        if num % 3 == 0:
            continue
        else:
            counter += 1
        # if (nums[i] + 1) % 3 == 0 or (nums[i] - 1) % 3 == 0:
        #     counter + 1
    return counter

    # another solution that is kind of like list comprehension
    # return sum(1 for n in nums if n % 3)

print(minimumOperations([1,2,3,4]))
        