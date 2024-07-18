def romanToInt(s: str) -> int:
    # create a dict for string:int
    roman_num_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # init output = 0
    output = 0
    # loop thru s
    for i in range(len(s)):
    # look up char in dict
        # having s[i + 1] if fine here because on the last loop, i = 6 and 6 is never < 7-1. so it never evaluates the second condition
        if i < len(s) - 1 and roman_num_dict[s[i]] < roman_num_dict[s[i + 1]]:
            # subtract the value from output
            output -= roman_num_dict[s[i]]
            print(f'{i}: subtract: {output}')
        else:
            output += roman_num_dict[s[i]]
            print(f'{i}: add: {output}')
        # output += roman_num_dict[s[i]]
    return output
print(romanToInt("MCMXCIV"))