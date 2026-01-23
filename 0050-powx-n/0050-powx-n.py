class Solution:
    def myPow(self, x: float, n: int) -> float:

        # 5^7 = 5^3 * 5^3 * 5^1 --------> 7 // 2
        # 5^3 = 5^1 * 5^1 * 5
        # a^c * b^c --> (a.b)^c  
        
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x * x, n//2)

            return res * x if (n % 2) else res
        
        answer = helper(x, abs(n))
        
        return answer if n>=0 else (1/answer)

        