class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = dict.fromkeys(nums, 0)
        for i in nums:
            numDict[i] += 1
        return sorted(numDict, key=numDict.get, reverse=True)[:k]
            
