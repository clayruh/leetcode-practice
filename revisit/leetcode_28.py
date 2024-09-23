def strStr(haystack, needle):
    # two strings to find first occurrence of needle IN haystack
    
    # conditions that immediately return a no:
    # if len(needle) > len(haystack)
    if len(needle) > len(haystack):
        return -1

    # loop through haystack
    for i in range(len(haystack)):
        # find a letter worth checking out for needle
        # if haystack[i] == needle[0]
        if haystack[i] == needle[0]:
            # check we're still in a valid range before indexing haystack
            # if i + len(needle) <= len(haystack) [range is up to but not including #]
            if i + len(needle) <= len(haystack):
                # check if index haystack[i:i + len(needle)] == needle
                if haystack[i:i + len(needle)] == needle:
                    # return i
                    return i
    return -1

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("happybutsad", "sad"))