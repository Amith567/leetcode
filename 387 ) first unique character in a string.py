class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
        for i,v in enumerate(s):
            if hashmap[v]==1:
                return i
        return -1
