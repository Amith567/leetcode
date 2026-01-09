class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq={}
        for item in stones:
            freq[item]=freq.get(item,0)+1
        count=0
        for i in jewels:
            if i in freq:
                count+=freq[i]
        return count
