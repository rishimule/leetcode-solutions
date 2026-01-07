class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n ==0 or n ==1:
            return n

        palindromeCount = 0

        for i in range(n):
            lc, rc = i, i

            while lc >=0 and rc < n and s[lc] == s[rc]:
                palindromeCount += 1
                lc -= 1
                rc += 1

        for i in range(n-1):
            lc, rc = i, i+1

            while lc >=0 and rc < n and s[lc] == s[rc]:
                palindromeCount += 1
                lc -= 1
                rc += 1

        return palindromeCount






        