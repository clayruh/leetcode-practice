def isSubsequence(s: str, t: str) -> bool:
    # check if characters of s are in t
    # characters of s have to be in order in t
    # modified_t = t
    if len(s) > len(t):
        return False
    # for char in s:
    #     if char not in t:
    #         return False
    # return True
 
    # for i in range(len(modified_t)):
    #     if s == modified_t:
    #         return True
    #     if modified_t[i] not in s:
    #         modified_t = modified_t.replace(modified_t[i], "")
    #         print(modified_t)
    # if s != modified_t:
    #     return False

    if not s:
        return True
    if not t:
        return False
    s_idx = t_idx = 0
    while t_idx < len(t) and s_idx < len(s):
        if t[t_idx] == s[s_idx]:
            s_idx += 1
        t_idx += 1
    return s_idx == len(s)
print(isSubsequence("aec", "abcde"))
