# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        # edge cases
        if len(s) != len(t):
            return False

        sCount = [0] * 26         
        tCount = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            sCount[idx] += 1

            idx = ord(t[i]) - ord("a")
            tCount[idx] += 1
        
        for i in range(26):
            if sCount[i] != tCount[i]:
                return False
        
        return True



