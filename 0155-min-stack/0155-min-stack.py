class MinStack:

    def __init__(self):
        # keep track of idx of the minimum in a stack
        # when a new minimum is added to the stack, map the idx of the previous
        # min to its idx (hint: since its a stack, the prev min idx 
        # will always be smaller)
        self.stack = []
        self.curMin = -1
        self.prevMin = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack or val <= self.stack[self.curMin]:
            self.prevMin[len(self.stack)-1] = self.curMin
            self.curMin = len(self.stack)-1
        
    def pop(self) -> None:
        if self.stack: 
            #update min
            if self.curMin == len(self.stack)-1:
                self.curMin = self.prevMin[self.curMin]
                del self.prevMin[len(self.stack)-1]
            self.stack.pop()
            
        
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.stack[self.curMin] if self.stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()