class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            oldLen = len(numSet)
            numSet.add(i)
            if len(numSet) == oldLen:
                return True
        return False