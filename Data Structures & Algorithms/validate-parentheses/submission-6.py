class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for ch in s:
            if ch == ")" or ch == "}" or ch == "]":
                if stack:
                    och = stack.pop()
                    if (ch == ")" and och != "(") or (ch == "]" and och != "[") or (ch == "}" and och != "{"):
                        return False
                        
                else:
                    return False
            else:
                stack.append(ch)

        return True if not stack else False