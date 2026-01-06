class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        a=s.split(' ')
        if len(a)!=len(pattern):
            return False
        a_b={}
        b_a={}
        for a1,b1 in zip(a,pattern):
            if a1 in a_b and a_b[a1]!=b1:
                return False
            if b1 in b_a and b_a[b1]!=a1:
                return False
            a_b[a1]=b1
            b_a[b1]=a1
        return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        return [words.index(a) for a in words]==[pattern.index(b) for b in pattern]
