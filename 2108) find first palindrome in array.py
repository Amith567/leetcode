class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            palindrome=word[-1::-1]
            if word==palindrome:
                return word
        return ""
        
