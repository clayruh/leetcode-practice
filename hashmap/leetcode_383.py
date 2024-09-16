
def canConstruct(ransomNote, magazine) -> bool:
#     # 4:06 - took abt two hours to figure out
#     # not all letters of magazine have to be used in ransomNote
#     # do the letters in magazine have to be in order in ransomNote too? (not sure)

#     # using two pointers that will move at different paces throughout the two words
#     idx_i = idx_j = 0

# # the idea is that we get to the end of ransomNote and we return True
#     while idx_i < len(ransomNote) and idx_j < len(magazine):
#         print(idx_i, ransomNote[idx_i], idx_j, magazine[idx_j])
#         # if the letters match, proceed through ransomNote
#         if magazine[idx_j] == ransomNote[idx_i]:
#             idx_i += 1
#         # proceed thru magazine
#         idx_j += 1
#     # once we're out of the while loop, if we haven't reached the end of ransomNote, return false
#     print(idx_i, idx_j)
#     if idx_i != len(ransomNote):
#         return False
#     else: 
#         return True
    

    # whelps looks like the order doesn't matter UGH
    # so we can run a create_dict function to make a dictionary out of the words {char:# of appearances}
    ransomNote_dict = {}
    magazine_dict = {}

    def createDict(string, dict):
        for char in string:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    createDict(ransomNote, ransomNote_dict)
    createDict(magazine, magazine_dict)
    print(ransomNote_dict, magazine_dict)
    # then loop through one dict and see if the value matches
    for char in ransomNote_dict:
        print(char)
        if char not in magazine_dict:
            print(f'{char} not in dict')
            return False
        if ransomNote_dict[char] > magazine_dict[char]:
            print(f'{char} count is greater than')
            return False
    return True
    # if not, return false at the first sight
    # else, return true
print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))