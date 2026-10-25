class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at opposite ends of the string
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # Skip non-alphanumeric characters from the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # Compare characters ignoring uppercase/lowercase
            # Return False if characters don't match
            if s[l].lower() != s[r].lower():
                return False

            # Move both pointers inward after matching
            l, r = l + 1, r - 1

        # All valid characters matched, so it's a palindrome
        return True

    def alphaNum(self, c):
        # Check if character is a letter (A-Z, a-z) or digit (0-9)
        # ord() converts a character to its ASCII/Unicode number
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

# Time: O(n) - Each pointer moves through the string at most once
# Space: O(1) - Only two pointers, no additional data structures