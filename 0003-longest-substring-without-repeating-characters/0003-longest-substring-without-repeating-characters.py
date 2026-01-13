class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        lp = 0
        rp = 0
        maxlen = 1
        

        while True:
            # if lp == len(s) - 1 and lp==rp:
            #     return maxlen

            if rp < len(s)-1:
                rp += 1
            else:
                return maxlen
            
            if s[rp] in s[lp:rp]:
                while s[lp] != s[rp]:
                    lp += 1
                lp += 1
            
            maxlen = max(maxlen, rp-lp+1)



        