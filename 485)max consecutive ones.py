class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=count=max_count=0
        for right in range(len(nums)):
            if nums[right]==0:
                left=right+1
            else: 
                count=right-left+1
                max_count=max(max_count,count)
        return max_count       
