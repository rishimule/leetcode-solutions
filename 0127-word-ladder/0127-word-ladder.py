class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0        

        # create adj list
        nei = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        def neighWords(word):
            res = []
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for w in nei[pattern]:
                    if w != word:
                        res.append(w)

            return res
        
        q = deque([(beginWord, 1)])
        visit = set()
        while q:
            word, t = q.popleft()
            if word == endWord:
                return t
            visit.add(word)
            for neiWord in neighWords(word):
                if neiWord not in visit:
                    q.append((neiWord, t+1))
        
        return 0

        