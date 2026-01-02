class Solution:
    def toLowerCase(self, s: str) -> str:
        s=list(s)
        for i in range(len(s)):
            if s[i].isupper():
                s[i]=s[i].lower()
        return "".join(s)
      

class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

class Solution:
    def toLowerCase(self, s: str) -> str:
        s=list(s)
        for index,i in enumerate(s):
            if ord(i) >64 and ord(i)<91:
                let=chr(ord(i)+32)
                s[index]=let
            
        return "".join(s)

