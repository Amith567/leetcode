class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=word.find(ch)
        if index==-1:
            return word
        else:
            s=list(word)
            word=s[index::-1]+s[index+1:]
            return "".join(word)

