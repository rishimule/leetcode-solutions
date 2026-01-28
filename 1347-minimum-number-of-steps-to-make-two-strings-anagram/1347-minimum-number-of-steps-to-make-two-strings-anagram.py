class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s) # {l:1, e:3, t:1, c:1, o:1, d:1}
        t_count = Counter(t) # {p:1, r:1, a:1, c:2, t:1, i:1, e:1}
        
        diff = 0
        for char in set(s+t):
            diff += abs(s_count[char] - t_count[char])
            '''
            l 1
            e 2
            t 0
            c 1
            o 1
            d 1
            p 1
            r 1
            a 1
            i 1
            ----
              10
              // 2
              ----
              5
            '''

        return diff // 2 

        