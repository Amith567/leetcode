class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        first_index={}
        for i,v in enumerate(nums):
            if v in first_index and i-first_index[v] <=k:
                return True
            first_index[v]=i
        return False
