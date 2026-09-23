class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        sDict = dict.fromkeys(list(s), 0)
        for i in s:
            sDict[i] += 1
        for i in t:
            if i not in sDict.keys():
                return False
            sDict[i] -= 1
            
        for i in sDict.keys():
            if sDict[i] != 0:
                return False
        return True
