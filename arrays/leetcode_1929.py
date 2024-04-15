def getConcatenation(nums):
    # essentially we want to iterate thru nums
    # create a new array that includes nums, then adds on a new exact copy of nums 
    ans = []
    for num in nums:
        ans.append(num)
    ans += nums
    # print(f'array {ans}')
    print(f'array {2*nums}')
    return ans

    # could also friggen just do return nums + nums or 2*nums


nums = [1,2,3]

getConcatenation(nums)