class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_t={}
        for i in t:
            dict_t[i]=dict_t.get(i,0)+1
        for ch in s:
            dict_t[ch]-=1
        for i,v in dict_t.items():
            if dict_t[i]>0:
                return i

