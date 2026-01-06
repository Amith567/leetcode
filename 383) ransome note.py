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

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        return not(Counter(ransomNote)-Counter(magazine))

from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag=defaultdict(int)
        for i in magazine:
            mag[i]+=1
        for ch in ransomNote:
            if mag[ch]==0:
                return False
            mag[ch]-=1
        return True
 
