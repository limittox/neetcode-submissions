class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        """
        operands will be from -200 to 200

        Q1: Can you have subsequent operators
        [1,2,+,-]
        Q2: Can it be many numbers until we reach an operator
            True
        Q3:After we encounter an operator, always the number of operands left in the list will be 1
        
        numbers = []
        for token in tokens:
            if token in operator:
                res = numbers.pop()
                i = len(numbers)-2
                while i >= 0:
                    if plus then:
                        add and pop
                    if minus
                        sub
                    if mul
                        ...
                    if divid
                        ...
                numbers.append(res)
                i -=1
                continue
            numbers.append(token)
            i-=1
        
        return numbers[-1]


        """

        numbers = []
        # res = 0

        for token in tokens:
            if token not in operators:
                numbers.append(int(token))
                continue
            
            right = numbers.pop()
            left = numbers.pop()


            if token == "+":
                res = left + right
            elif token == "-":
                res = left - right
            elif token == "*":
                res = left * right
            else:
                res = int(left / right)

            numbers.append(res)

        return numbers[-1]

