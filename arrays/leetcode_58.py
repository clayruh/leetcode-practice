def lengthOfLastWord(s):
    # split string by spaces returns a list of strings
    s_as_list = s.split(" ")
    # still need to account for multiple spaces
    print(s_as_list)
    for i in range(len(s_as_list))[::-1]:
        if s_as_list[i] != '':
            return len(s_as_list[i])

print(lengthOfLastWord("Hello World"))