def merge(nums1, m, nums2, n):
    # keep track of indices 
    nums2_idx = 0
    starting_idx = m
    for i in range(starting_idx, m+n):
        nums1[i] = nums2[nums2_idx]
        nums2_idx += 1
    # new_list = sorted(nums1)
    nums1.sort()
        
    return nums1