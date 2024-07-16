def summaryRanges(nums):
    # # sorted unique array nums
    # # parse through nums and return the smallest sorted list
    # start_idx = end_idx = 0
    # # have a loop to look at our initial num
    # # then continue to end_idx until end of a range
    # output = []
    # for i in range(1, len(nums)):
    #     print(f'start_num: {nums[start_idx]} end_num: {nums[end_idx]} i: {i} start_idx: {start_idx} end_idx: {end_idx}')
    #     if nums[i] - nums[i-1] == 1:
    #         end_idx += 1
    #         continue
    #     # if we've reached this line, it's that we've finished our range or that the number is itself
    #     if nums[start_idx] == nums[end_idx]:
    #         output.append(f'{nums[i]}')
    #     else:
    #         output.append(f'{nums[start_idx]}->{nums[end_idx]}')
    #         print(f'output: {output}')
    #         start_idx = end_idx = i
    #         print(f'start_idx: {start_idx} end_idx: {end_idx}')
    # return output

        # we don't care about the indices, so we're starting with the actual nums
        output = []
        start_num = end_num = nums[0]
        for i in range(1, len(nums)):
            # case1: nums[i] - end_num == 1 then we change end_num to nums[i]
            # continue
            if nums[i] - end_num == 1:
                end_num = nums[i]
                continue

            # case2: if start_num == end_num
            # output.append(f'{start_num}')
            if start_num == end_num:
                output.append(f'{start_num}')

            # case3: start_num != end_num AND we've reached the end of a valid range
            # output.append(f'{start_num}->{end_num}')
            else:
                output.append(f'{start_num}->{end_num}')
            
            # update start_num and end_num to nums[i]
            start_num = end_num = nums[i]
            print(f'start_num: {start_num}, end_num: {end_num}, i: {i}')
        print(start_num, end_num)
        if start_num == end_num:
            output.append(f'{start_num}')
        else:
            output.append(f'{start_num}->{end_num}')
        return output

print(summaryRanges([0,2,3,4,6,9]))