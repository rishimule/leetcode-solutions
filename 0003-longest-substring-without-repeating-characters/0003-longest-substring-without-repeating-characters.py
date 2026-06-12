class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #edge cases
        if len(s) < 2:
            return len(s)

        res = 1
        l = 0
        r = 1
        
        bucket = set(s[0])

        while r < len(s):
            
            if s[r] not in bucket:
                bucket.add(s[r])
            else:
                #update l until we remove the duplicate
                while s[l] != s[r]:
                    bucket.remove(s[l])
                    l += 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1
        
        return res

        