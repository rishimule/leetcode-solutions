class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for p in details:
            count += 1 if int(p[11:13]) > 60 else 0
        return count
        