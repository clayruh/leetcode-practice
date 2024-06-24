def isIsomorphic():
# initiate dictionary, O(1) runtime
    isomorphic_dict = {}
    letters_seen = set()
# checking if the length of s and t are the same
    if len(s) != len(t):
        return False
    for i in range(len(s)):
# checking dict for s[i] != t[i]
        
# if s[i] is not in the dict, this results in a KeyError, so we have to check it's in the dict first
        if s[i] in isomorphic_dict and isomorphic_dict[s[i]] != t[i]:
            return False
        
# if letter is not, create key:value pair
        if s[i] not in isomorphic_dict:
            if t[i] in letters_seen:
                return False
            isomorphic_dict[s[i]] = t[i]
            letters_seen.add(t[i])
    return True
            
            
# s = "badc" t = "baba"