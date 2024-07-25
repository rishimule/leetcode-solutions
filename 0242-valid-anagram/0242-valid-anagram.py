class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h = {}
        for l in s:
            if l in h:
                h[l] += 1
            else:
                h[l] = 1
        
        for l in t:
            if l in h:
                if h[l] > 0:
                    h[l] -= 1
                else:
                    return False
            else:
                return False
        
        if sum(h.values()) == 0:
            return True
        else:
            return False