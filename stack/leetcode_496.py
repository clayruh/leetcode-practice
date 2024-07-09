def nextGreaterElement(nums1, nums2):
# loop through nums1: for num in nums1
# make nums2 into a dictionary? {1:0,3:1,4:2,2:3}
# lookup num in dict, then find nums_in_nums2 = nums2[dict[num] + 1]
# if num_in_nums2 > num, ans.append(num_in_nums2), else ans.append(-1)
    nums2_dict = {}
    ans = []

    for i in range(len(nums2)):
        nums2_dict[nums2[i]] = i
    print(nums2_dict)
        
    # while i < range(len(nums1)-1):
    for num in nums1:
        print(f'num1: {num}')
        found = False
        nums2_index = nums2_dict[num]
        starting_idx = nums2_index + 1
        end_of_nums2 = len(nums2)
        for i in range(starting_idx, end_of_nums2):
            print(f'\t next num in nums2: {nums2[i]}')
            if nums2[i] > num:
                ans.append(nums2[i])
                found = True
                break
        if not found:
            ans.append(-1)


        # next_num = nums2[nums2_dict[num] + 1]
        # if nums_in_nums2 > num:
        #     ans.append(nums_in_nums2)
        # else:
        #     ans.append(-1)
    return ans
    
print(nextGreaterElement([4,1,2],[1,3,4,2]))

[3,4,1]
[1,3,2,4]