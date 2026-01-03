class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for v in nums:
            if v in hashmap:
                hashmap[v]+=1
            else:
                hashmap[v]=1
        return True if max(hashmap.values())>1 else False
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for v in nums:
            if v in hashmap:
                return True
            hashmap[v]=1
        return False

        
