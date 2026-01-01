class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)==1:
            return 0
        left=0
        right=len(needle)
        while right-1<len(haystack):
            if needle==haystack[left:right]:
                return left
            else:
                left+=1
                right+=1
        return -1
