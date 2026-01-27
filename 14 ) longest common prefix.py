# using horizontal scaning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for s in strs[1:]:
            while s[:len(prefix)]!=prefix:
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for i in range(len(prefix)):
            for word in strs[1:]:
                if i>=len(word) or word[i]!=prefix[i]:
                    return prefix[:i]
        return prefix


        
        
