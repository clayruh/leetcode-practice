import collections
def intersect(nums1, nums2):
    intersect_array = []
    # using collections.Counter, create hashmap of number of times each integer appears for both nums1 and nums2
    nums1_count = collections.Counter(nums1)
    nums2_count = collections.Counter(nums2)
    # loop through nums1_count
    for key in nums1_count:
        if key in nums2_count:
            # getting the minimum number of appearances (value) of either array
            appearance = min(nums1_count.get(key), nums2_count.get(key))
            # using extend method because there could be multiple appearances of a key
            intersect_array.extend([key] * appearance)

    return intersect_array