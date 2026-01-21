class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #TODO: Null Check

        stack1 = [i for i in s]

        stack2 = [stack1.pop()]

        count = 1

        while True:
            stack1lenprior = len(stack1)
            while stack1:
                last = stack1.pop()

                if stack2 and last == stack2[-1]:
                    count += 1
                else:
                    count = 1

                stack2.append(last)

                if count == k:
                    for _ in range(k):
                        stack2.pop()
                    count = 1
                
            if len(stack2) < stack1lenprior:
                #we still need to go
                while stack2:
                    stack1.append(stack2.pop())
            else:
                return "".join(stack2[::-1])
          
        return s
            
            



        