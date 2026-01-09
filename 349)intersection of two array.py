class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        freq={}
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        for j in nums2:
            if j in  freq and j not in res:
                res.append(j)
        return res
