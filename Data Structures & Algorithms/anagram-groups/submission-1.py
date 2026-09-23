class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gramsDict = dict()
        for i in strs:
            sortedI = ''.join(sorted(list(i)))
            if not sortedI in gramsDict.keys():
                gramsDict[sortedI] = [i]
            else:
                gramsDict[sortedI].append(i)
        return list(gramsDict.values())