class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        res = sorted(res.items(), key= lambda x: x[1], reverse= True)
        return [num for num, index in res[:k]]

        