class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p=sorted(p)
        k=len(p)
        res=[]
        if len(p)>len(s):
            return []
        for i in range(len(s)-k+1):
            window=s[i:i+k]
            if sorted(window)==p:
                res.append(i)
        return res
