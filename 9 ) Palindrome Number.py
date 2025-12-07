# using reverse string  method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        return True if y==y[::-1] else False

# using reverse integer method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        org=x
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        return org==rev

