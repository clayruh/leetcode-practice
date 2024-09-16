def longestCommonPrefix(strs) -> str:
    prefix = ""
    ref_word = strs[0]
    for i in range(1, len(strs)):
        if ref_word[0] != strs[i][0]:
            return prefix
        

    return