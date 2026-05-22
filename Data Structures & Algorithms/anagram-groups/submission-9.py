class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        final = list()
        for ele in strs:
            ts = "".join(sorted(ele))
            if ts in temp:
                temp[ts].append(ele)
            else:
                temp[ts] = [ele]

        return list(temp.values())
