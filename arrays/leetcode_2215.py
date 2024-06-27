def findDifference(nums1, nums2):
    # answer is going to be [distinct int in nums1 not in nums2] [distinct int in num2 not in nums1]
    answer = []
    # two diff lists to track which numbers don't show up in either array
    # not_in_nums1 = []
    # not_in_nums2 = []
    # could make nums1 and nums2 into sets to make sure all the numbers are distinct
    nums1_set = set(nums1)
    nums2_set = set(nums2)
    # for num in nums1_set:
    #     if num not in nums2_set:
    #         not_in_nums2.append(num)
    not_in_nums2 = [num for num in nums1_set if num not in nums2_set]
    # for num in nums2_set:
    #     if num not in nums1_set:
    #         not_in_nums1.append(num)
    not_in_nums1 = [num for num in nums2_set if num not in nums1_set]

    answer.append(not_in_nums2)
    answer.append(not_in_nums1)
    print(nums1_set)
    print(nums2_set)
    print(not_in_nums1)
    print(not_in_nums2)
    print(answer)
    return answer

findDifference([1,2,3], [2,4,6])