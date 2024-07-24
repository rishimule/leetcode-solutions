class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 != 0:
            return -1
        
        count = {
            "c" : 0,
            "r" : 0,
            "o" : 0,
            "a" : 0,
            "k" : 0,
        }
        prec = {
            "r" : "c",
            "o" : "r",
            "a" : "o",
            "k" : "a",
        }
        
        frogs = 0
        
        for s in croakOfFrogs:
            
            if s != "c":
                if count[prec[s]] > 0:
                    count[prec[s]] -= 1
                else:
                    return -1
            else:
                if count["k"] > 0:
                    count["k"] -= 1
                else:
                    frogs += 1
            count[s] += 1
            
            # print(count)
    
        return frogs if sum(count.values()) - count["k"] == 0 else -1
  
        
