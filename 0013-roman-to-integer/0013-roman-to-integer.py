class Solution:
    def romanToInt(self, s: str) -> int:
        translate = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        output = 0

        for i in range(len(s)-1):
            if translate[s[i]] >= translate[s[i + 1]]:
                output += translate[s[i]]
            else:
                output -= translate[s[i]]
        
        output += translate[s[-1]]

        return output
        