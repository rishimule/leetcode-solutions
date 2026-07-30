class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = defaultdict(list)

        for word in strs:
            sortedMap["".join(sorted(word))].append(word)
        
        return list(sortedMap.values())
        