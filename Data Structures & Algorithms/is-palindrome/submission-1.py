class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:
            # Skip non-alphanumeric characters from the left
            while i < j and not self.alphaNum(s[i]):
                i += 1

            # Skip non-alphanumeric characters from the right
            while i < j and not self.alphaNum(s[j]):
                j -= 1

            # Compare characters ignoring uppercase/lowercase
            if s[i].lower() != s[j].lower():
                return False

            # Move both pointers inward
            i, j = i + 1, j - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))