class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = dict.fromkeys(nums, 0)
        for i in nums:
            numDict[i] += 1
        output = []
        for i in range(k):
            output.append(sorted(numDict, key=numDict.get, reverse=True)[i])
        return output
            
