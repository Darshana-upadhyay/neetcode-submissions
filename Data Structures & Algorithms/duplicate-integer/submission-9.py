class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setl= set()
        for i in nums:
            if i in setl:
                return True
            setl.add(i)
        return False