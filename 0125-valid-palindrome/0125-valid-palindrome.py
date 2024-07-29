class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l=0
        r= n-1
        
        while l<r:
            if s[l].isalnum() == True:
                if s[r].isalnum() == True:
                    if s[l].lower() != s[r].lower():
                        return False
                    else:
                        l += 1
                        r -= 1
                else:
                    r -= 1
            else:
                l += 1
        
        return True
   
# st = "A man, a plan, a canal: Panama"
# s = Solution()
# s.isPalindrome(st)