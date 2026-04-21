class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        final = dict()
        duplicate = list()
        for item in strs:
            if item not in temp:
                temp[item] = []
            temp[item].append("".join(sorted(list(item))))
        
        print(temp)
        for key, value in temp.items():
            if value[0] not in final:
                final[value[0]]=[]
            for v in value:
                final[value[0]]. append(key)
        

        return list(final.values())
