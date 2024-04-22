
def intersect(nums1, nums2):
    # return an array of nums1 and nums2 intersections, documenting repeats
    intersect_nums = []

    def shorterArray(nums1, nums2):
        return (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

    shorter_array, longer_array = shorterArray(nums1, nums2)
    for num in shorter_array:
        print(f'num: {num}')
        if num in longer_array:
            print(f'appending: {num}')
            intersect_nums.append(num)
    print(intersect_nums)
    return intersect_nums
    
intersect([3,1,2], [1,1])
# with this example, we get [1,1], which is incorrect