class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        res = 1
        seq = list()
        print(nums)
        for i in range(len(nums)):
            if i != len(nums)-1:
                if nums[i] + 1 == nums[i+1]:
                    res = res + 1
                else:
                    seq.append(res)
                    res = 1
            else: #for last element
                seq.append(res)
        return max(seq) if seq else 0