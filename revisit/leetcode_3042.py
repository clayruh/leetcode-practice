class Solution(object):
    def countPrefixSuffixPairs(self, words):
        # had to have ChatGPT help me through this problem... I get it now, but definitely came nowhere close to this answer
        def isPrefixAndSuffix(str1, str2):
            # if prefix + suffix of str2 matches str1, return True
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            # otherwise return False
            else:
                return False
            
        count = 0
        # this is a loop within a loop, which has an (O)n^2, not a good thing
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count