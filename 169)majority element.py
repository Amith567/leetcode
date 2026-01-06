from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        midlen=len(nums)//2
        counter=Counter(nums)
        for v in counter:
            if counter[v]>midlen:
                return v
