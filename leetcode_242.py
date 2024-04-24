def isAnagram(s,t):
    # make s and t into arrays
    # while loop? while len(s_as_array) > 0
    # loop through string t as array list(t)
    # check that the letter of t is in s
    # if it isn't, return False
    # else:
    # for every letter in t that matches s, remove the letter
    # once len(s_as_array) = 0 we know all the letters of t match letters of s
    s_as_array = list(s)
    t_as_array = list(t)

    while len(s_as_array) > 0:
        for letter in t_as_array:
            # print(f'{letter}')
            if letter not in s_as_array or len(t_as_array) < len(s_as_array):
                # print(f'false')
                return False
            else:
                # print(f'removing letter {letter} from s')
                # print(f't: {t_as_array} s: {s_as_array}')
                s_as_array.remove(letter)
    # print(f'true')
    return True

s = "aa"
t = "a"

isAnagram(s,t)