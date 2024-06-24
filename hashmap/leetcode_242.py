# collections.Counter(string, list, etc) returns a dict w a counter of every thing, and how many times it appears
import collections

# "saabcgaab"
{"s":1,
 "a":4,
 "b":2,
"c":1,
"g":1,
 }

def isAnagram(s,t):
    # s_as_dict = collections.Counter(s)
    # t_as_dict = collections.Counter(t)

    # if s_as_dict != t_as_dict:
    #     return False
    # return True

    return collections.Counter(s) == collections.Counter(t)