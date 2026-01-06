
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t={}
        t_s={}
        for i1,i2 in zip(s,t):
            if i1 in s_t and s_t[i1]!=i2:
                return False
            if i2 in t_s and t_s[i2]!=i1:
                return False
            s_t[i1]=i2
            t_s[i2]=i1
        return True
