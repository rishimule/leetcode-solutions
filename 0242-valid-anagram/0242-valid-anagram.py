class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # # nUll check
        # if len(s) != len(t):
        #     return False

        # # count = {}
        
        # # for i in range(len(s)):
        # #     if s[i] not in count:
        # #         count[s[i]] = 0
        # #     count[s[i]] += 1
        
        # count_s = Counter(s)
        # count_t = Counter(t)

        # diff= 0
        # for char in set (s + t):
        #     diff += abs(count_s[char] - count_t[char])
        
        # return True if not diff else False


        