class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(sorted(set(nums)))
        res = 1
        longest = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                res = res + 1
            else:
                longest = max(longest,res)
                res = 1
        longest = max(longest,res)
        return longest