class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for i,v in freq.items():
            if v<2:
                return i
