class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        result = defaultdict(int)
        for i in nums:
            result[i] += 1
        fin = dict(sorted(result.items(), key=lambda item: item[1], reverse= True))
        print(fin)
        return list(fin.keys())[:k]