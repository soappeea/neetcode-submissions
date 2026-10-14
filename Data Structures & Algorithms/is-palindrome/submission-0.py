class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum(): # Detects if c is alphanumeric
                newStr += c.lower()
        
        return newStr == newStr[::-1] # [::-1] reverses string

        
