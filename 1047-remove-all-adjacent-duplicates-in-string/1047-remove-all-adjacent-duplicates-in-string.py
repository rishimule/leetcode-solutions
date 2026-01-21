class Solution:
    def removeDuplicates(self, s: str) -> str:
        #TODO: Null check
        if len(s) <= 1:
            return s
        
        # use stack
        stack = [s[0]]
        for letter in s[1:]:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)