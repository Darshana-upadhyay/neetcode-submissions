class Solution:
    def isValid(self, s: str) -> bool:
        sl = list()
        for i in s:

            if i == ')' or i == '}' or i == ']':
                if sl and i == ')' and sl[-1] == '(':
                    sl.pop(-1)
                elif sl and i == '}' and sl[-1] == '{':
                    sl.pop(-1)
                elif sl and i == ']' and sl[-1] == '[':
                    sl.pop(-1)
                else:
                    return False
            else:
                sl.append(i)
        if sl:
            return False
        return True

                
