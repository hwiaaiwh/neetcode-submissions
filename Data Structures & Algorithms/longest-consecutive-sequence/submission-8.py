class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        newNums = sorted(list(set(nums)))
        print(newNums)
        c = 1
        tmp = 1
        
        for i in range(len(newNums) - 1):
            if newNums[i] == newNums[i+1] - 1:
                tmp += 1
            else:
                c = max(c, tmp)
                tmp = 1
        return max(c, tmp)
