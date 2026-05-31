class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for ele in strs:
            count = [0] * 26
            for ch in ele:
                count[ord(ch)- ord('a')] += 1
            key = tuple(count)
            res[key].append(ele)
        return list(res.values())

