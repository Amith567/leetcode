class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window=sum(nums[:k])
        max_val=window
        for i in range(k,len(nums)):
            window+=nums[i]
            window-=nums[i-k]
            max_val=max(max_val,window)
        return max_val/k
        
