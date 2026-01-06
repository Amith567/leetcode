class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in s:
            hashmap[i]=hashmap.get(i,0)+1
        for i,v in enumerate(s):
            if hashmap[v]==1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import defaultdict
        counter=defaultdict(int)
        for ch in s:
            counter[ch]+=1
        for i,v in enumerate(s):
            if counter[v]==1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counter=Counter(s)
        for i,v in enumerate(s):
            if counter[v]==1:
                return i
        return -1
