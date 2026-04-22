class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s))
            res += ","
        res = res[:-1] + "#"
        encoded = "".join(strs)
        res = res + encoded
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = s.split("#")[0]
        s= s[len(sizes)+1:]
        res = []
        i = 0
        print(s)
        for n in sizes.split(","):
            temp = int(n) + i
            word = s[i:temp]
            i += int(n)
            res.append(word)
        return res




        





