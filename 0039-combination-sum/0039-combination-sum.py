class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = []


        def backtrack(remain, path, start):
            if remain == 0:
                result.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i)
                path.pop()        

        backtrack(target, [], 0)
        return result