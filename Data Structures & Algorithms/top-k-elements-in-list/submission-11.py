class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fd = defaultdict(int)
        for num in nums:
            fd[num] += 1
        final = sorted(fd.items(), key = lambda x : x[1], reverse=True)
        
        return [key for key, value in final[:k]]

        