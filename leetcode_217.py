class Solution:
    def containsDuplicate(self, nums):
        checking_nums = set()
        # iterate through nums
        for num in nums:
        # append each number to checking_nums
        # check if that number is already in checking_nums
            if num in checking_nums:
                return True
            else:
                checking_nums.add(num)
            # if num not in checking_nums:
            #     checking_nums.append(num)
            # else:
            #     return True
        # if the number is, return True
        # if the number isn't, return False
        return False