class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        i = 0
        n = 1
        for i in range(len(nums)-1):
            if sorted_nums[i] == sorted_nums[n]:
                return True
            i += 1
            n += 1

        return False