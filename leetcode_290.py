def wordPattern(pattern: str, s: str) -> bool:
    # initialize pattern_dict 
    pattern_dict = {}
    # process string s (aka loop)
        # if char == " "
        # append string_chunk to list words
    words_list = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            words_list.append(word)
            word = ""
    words_list = s.split(" ") #split makes an array of strings 
        # print(word, words_list)
    if len(pattern) != len(words_list):
        return False
    # loop through pattern:
    for i in range(len(pattern)):
        # if char in pattern_dict:
        if pattern[i] in pattern_dict:
            print(pattern_dict)
            # if words[i] != pattern_dict[char]:
            if pattern_dict[pattern[i]] != words_list[i]:
                print(char, pattern_dict[pattern[i]], i,words_list[i])
                return False
        else:
            pattern_dict[pattern[i]] = words_list[i]
    return True

print(wordPattern("abba", "dog cat cat fish"))