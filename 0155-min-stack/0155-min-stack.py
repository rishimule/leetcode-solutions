class MinStack:

    def __init__(self):
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