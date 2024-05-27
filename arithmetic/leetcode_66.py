def PlusOne(digits):
    # if the last digit in the list isn't a 9,
    # digits[-1] += 1
    if digits[-1] != 9:
        digits[-1]+= 1
        return digits
    # from here we can make the list into an actual number 
    # then +1, and remake into a list
    multiplier = 1
    sum_of_digits_list = 0
    for digit in digits[::-1]:
        sum_of_digits_list += digit * multiplier
        multiplier *= 10
    print(sum_of_digits_list)

    sum_of_digits_list += 1
    number_as_list = []

    while sum_of_digits_list > 0:
        digit = sum_of_digits_list % 10 
        number_as_list.append(digit)
        sum_of_digits_list //= 10
    print(number_as_list[::-1])
    return number_as_list[::-1]

PlusOne([5,9,9,9,9,8,9])