class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in {"+", "-", "*", "/"}:
                stack.append(int(tokens[i]))
            else:
                elem2 = stack.pop()
                elem1 = stack.pop()

                if tokens[i] == "+":
                    num = elem1 + elem2
                elif tokens[i] == "-":
                    num = elem1 - elem2
                elif tokens[i] == "*":
                    num = elem1 * elem2
                elif tokens[i] == "/":
                    num = int(elem1 / elem2)
                
                stack.append(num)
        
        return stack[0]