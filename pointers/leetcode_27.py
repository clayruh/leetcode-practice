def removeElement(nums, val) -> int:
    index = 0
    for i in range(len(nums)):
        # replace the nums once we find a valid integer that's not the val
        if nums[i] != val:
            # doesn't matter what numbers comes after, so numbers that == val could appear, but it has to be after nums[index]
            nums[index] = nums[i]
            index += 1
    return index

print(removeElement([3,2,2,3], 3))