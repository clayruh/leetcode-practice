
def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    result = []

    shorter_list, longer_list = whichList(nums1, nums2)
    # python allows u to store multiple return values as multiple variables

    for num in shorter_list:
        if num in longer_list:
            result.append(num)
    print(result)
    return result

    # if len(nums1_as_set) < len(nums2_as_set):
    #     # compare against nums 2
    #     for num in nums1_as_set:
    #         if num in nums2_as_set:
    #             result.append(num)
    # else:
    #     for num in nums2_as_set:
    #         if num in nums1_as_set:
    #             result.append(num)
    # print(result)
    # return result

# take 2 lists, should return 1st list (shorter) 2nd list (longer)
def whichList(nums1, nums2):
    return (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

    # if len(nums1) <= len(nums2):
    #     return nums1, nums2
    # return nums2, nums1

    # if len(nums1) <= len(nums2):
    #     shorter_list = nums1
    #     longer_list = nums2
    # if len(nums2) <= len(nums1):
    #     shorter_list = nums2
    #     longer_list = nums1
    # return shorter_list, longer_list

intersection([1,2,3,5,6,24,10], [1,5,4,6,7,10])

