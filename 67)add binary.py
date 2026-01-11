class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1=int(a,2)
        num2=int(b,2)
        sum=bin(num1+num2)
        binary=sum[2:]
        return binary
        
