def buildArray(nums):
    ans = []
    # return the answer where nums[nums[i]]
    # for loop through nums
    for i in range(len(nums)):
        # print(f'i: {i}')
    # insert nums[i] into ans at nums[i]
        new_idx = nums[i]
        # print(f'number to insert: {nums[new_idx]} at {nums[i]}')
        new_num = nums[new_idx]
        ans.insert(i, new_num)
        # print(ans)
    return ans

print(buildArray([0,2,1,5,3,4]))