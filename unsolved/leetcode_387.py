class Solution(object):
    def firstUniqChar(self, s):
        # sets are the fastest runtime for data lookup (O(1))
        uniqueCharacters = {}
        # for i in range(len(s)):
            

        # return 
        
    s = "leetcode"
    {
        0: "l",
        1: "e",
        2: "e",
        3: "t",
        4: "c",
        5: "o",
        6: "d",
        7: "e",
    }

def addDuplicateChar(string):
    alreadySeen = set()
    repeatingChar = []
    for character in string:
        if character not in alreadySeen:
            alreadySeen.add(character)
            continue
        if character not in repeatingChar:
            repeatingChar.append(character)
        print("character should be in UniqueChar", alreadySeen, character, character in alreadySeen, repeatingChar)
        
    return repeatingChar

sentence = "iloveleetcodelots"
print(addDuplicateChar(sentence))

