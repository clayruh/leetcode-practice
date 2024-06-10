class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
# break up s into words separated by the spaces + store in a list
        words_in_s = s.split()
        print(words_in_s)
        word_pattern_dict = {}
        existing_values = set()
        
        if len(words_in_s) != len(pattern):
            return False
# initialize a dictionary based on the pattern
        for i in range(len(words_in_s)):
# check if the letter exists and matches the word of words_in_s[#]
            if pattern[i] in word_pattern_dict and word_pattern_dict[pattern[i]] != words_in_s[i]:
#  if the returl False doesn't happen, we can assume we've never seen the letter before
# or the letter : word are the same, so keep going
                return False


# edge case: "abba" "dog dog dog dog"
# we gotta check that dictionary[letter] doesn't exist AND the value is added to our set for tracking existing values
            if words_in_s[i] in existing_values and pattern[i] not in word_pattern_dict:
                return False
    
    
# if letter doesn't exist, add new letter:word pair
            word_pattern_dict[pattern[i]] = words_in_s[i]
            existing_values.add(words_in_s[i])
             
        return True
    
    