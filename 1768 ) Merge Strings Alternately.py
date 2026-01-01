class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                res+=word1[i]
            if i<len(word2):
                res+=word2[i]
        return res            

        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i in range(min(len(word1),len(word2))):
            s+=word1[i]
            s+=word2[i]
        s+=word1[i+1:]
        s+=word2[i+1:]
        return s

# two pointer method
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=right=0
        res=[]
        while left<len(word1) or right<len(word2):
            if left<len(word1):
                res.append(word1[left])
                left+=1
            if right<len(word2):
                res.append(word2[right])
                right+=1
        return "".join(res)

