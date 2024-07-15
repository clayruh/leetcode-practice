def findPermutationDifference(s: str, t: str) -> int:
    # create dictionary for both s and t, mapping char to index
    # then run arithmetic of like abs(s_val - t_val) and add all of them together for range(len(s))

    s_dict = {}
    t_dict = {}
    total = 0
    for i in range(len(s)):
        s_dict[s[i]] = i
    for i in range(len(t)):
        t_dict[t[i]] = i

    for char in s:
        total += abs(s_dict[char] - t_dict[char])
    return total
        
print(findPermutationDifference("abcde", "edbac"))