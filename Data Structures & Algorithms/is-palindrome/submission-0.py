class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for ele in s:
            if ele.isalnum():
                if ele.isdigit():
                    clean.append(ele)
                else:
                    clean.append(ele.lower())
        print(clean)
        j = len(clean) - 1
        for i in range(len(clean)//2):
            if clean[i] != clean[j]:
                return False
            j -= 1
        return True


        