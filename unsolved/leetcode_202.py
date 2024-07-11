def isHappy(n):
    # if n <9, return false
    if n <= 9:
        return False
    # in what case would the number does not end in 1?

    # turn n into a string and split it up
    if n >= 10:
        num = str(n)
        changing_sum = 0
        # loop thru num, 'cause it may be 2, 3, etc integers
        # maybe a while loop that feeds the loop until changing_sum < 10? then the integers cannot be squared
        # or something like while n > 9?
        while len(str(changing_sum)) >= 2:
            for integer in num:
                changing_sum += int(integer)**2
                print(integer)
                print(changing_sum)


    return

isHappy(19)