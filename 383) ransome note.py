class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magcounter={}
        notecounter={}
        for i in magazine:
            magcounter[i]=magcounter.get(i,0)+1
        for j in ransomNote:
            notecounter[j]=notecounter.get(j,0)+1
        for ch in notecounter:
            if ch not in magcounter or notecounter[ch]>magcounter[ch]:
                return False
        return True
