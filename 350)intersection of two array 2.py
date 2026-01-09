class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        res=[]
        for num in nums1:
            freq[num]=freq.get(num,0)+1
        for i in nums2:
            if i in freq and freq[i]>0:
                res.append(i)
                freq[i]-=1
        return res
