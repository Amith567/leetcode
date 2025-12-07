# using brute force
class Solution:   
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j] 
# using hashmap
class Solution:   
    def twoSum(self,nums,target):
        hashmap={}
        for index,value in enumerate(nums):
            complement=target-value
            if complement in hashmap:
                return hashmap[complement],index
            hashmap[value]=index
# using two pointer            
class Solution:   
    def twoSum(self,nums,target):
        arr=[(value,index) for index,value in enumerate(nums)]
        arr.sort()
        left=0
        right=len(arr)-1
        while left<right:
            sum=arr[left][0]+arr[right][0]
            if target==sum:
                return arr[left][1],arr[right][1]
            elif sum<target:
                left+=1
            else:
                right-=1
