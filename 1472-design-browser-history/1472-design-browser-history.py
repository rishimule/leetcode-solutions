class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.idx = 0
        self.len = 1
        

    def visit(self, url: str) -> None:
        if len(self.hist) <= self.idx + 1:
            self.hist.append(url)
        else:
            self.hist[self.idx+1] = url
        self.idx += 1
        self.len = self.idx + 1

        

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx-steps)
        return self.hist[self.idx]
        

    def forward(self, steps: int) -> str:
        self.idx = min(self.len -1, self.idx + steps)
        return self.hist[self.idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)