class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for ele in strs:
            key = "".join(sorted(ele))
            res[key].append(ele)
        return list(res.values())

