class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        freq={}
        for i in candyType:
            freq[i]=freq.get(i,0)+1
        if len(freq.keys())<n:
            return len(freq.keys())
        else:
            return n
        
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy=len(set(candyType))
        return min(candy,len(candyType)//2)
        
