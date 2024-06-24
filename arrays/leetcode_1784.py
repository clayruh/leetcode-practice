class Solution:
    def checkOnesSegment(self, s: str) -> bool:
# string will always start with 1s
# 1s cannot show up after 0s
# string cannot start with 0s

        have_we_seen_zero = False
        if s[0] == "0":
            return False
        for i in range(len(s)):
            if s[i] == "0":
                have_we_seen_zero = True
            if have_we_seen_zero == True and s[i] == "1":
                return False
        return True
            