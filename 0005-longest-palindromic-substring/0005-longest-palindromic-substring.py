class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = "babad", "abbd"

        n = len(s)

        if n == 0:
            return ""
        if n ==1:
            return s
        
        maxres = s[0]

        def checkMaxPalinCenter(s, n, cl, cr):
            # check if it is the center of palindrome
            le = cl-1
            re = cr+1
            res = s[cl:cr+1]
        
            while True:
                if le < 0 or re >= n or s[le] != s[re]:
                    break
                else:
                    res = s[le:re+1]
                    le = le-1
                    re = re+1
    
            return res

        for i in range(n):
            res = checkMaxPalinCenter(s,n,i,i)
            if len(res) > len(maxres): 
                maxres = res 
            
            if i < n-1:
                if s[i+1] == s[i]:
                    res = checkMaxPalinCenter(s,n,i,i+1)
                if len(res) > len(maxres): 
                    maxres = res 

        
        return maxres



            
