class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(sorted(set(nums)))
        res = 1
        longest = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                res = res + 1
            else:
                longest = max(longest,res)
                print(res)
                res = 1
        longest = max(longest,res)
        return longest