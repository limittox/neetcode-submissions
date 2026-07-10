class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketRef = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        closingBrackets = {")", "]", "}"}

        for b in s:
            if len(stack) == 0:
                stack.append(b)
                continue
            
            if b in closingBrackets and stack[-1] == bracketRef[b]:
                stack.pop()
                continue

            stack.append(b) 
        
        return True if len(stack) == 0 else False