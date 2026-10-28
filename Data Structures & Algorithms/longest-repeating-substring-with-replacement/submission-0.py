class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Store frequency of each character in current window
        count = {}
        res = 0
        l = 0

        # Highest character frequency seen as the window grows
        maxf = 0

        # Expand window by moving right pointer
        for r in range(len(s)):
            # Add current character to frequency dictionary
            count[s[r]] = 1 + count.get(s[r], 0)

            # Update highest frequency seen
            maxf = max(maxf, count[s[r]])

            # Window size - max frequency = replacements needed
            # Shrink window if replacements exceed k
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # Update longest valid length found
            res = max(res, r - l + 1)

        return res

    # Time: O(n) - Each pointer moves right at most n times
    # Space: O(1) - At most 26 keys for uppercase English letters