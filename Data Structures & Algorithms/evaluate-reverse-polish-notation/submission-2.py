class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = list()
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                a = s.pop()
                b = s.pop()

                if token == '+':
                    c = a + b
                elif token == '-':
                    c = b - a
                elif token == '*':
                    c = a * b
                else:
                    c = b / a

                s.append(int(c))

            else:
                s.append(int(token))
        return s.pop() if s else 0
