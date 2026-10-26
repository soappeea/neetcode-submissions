class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store each character's most recent index (char -> index)
        mp = {} 
        l = 0
        res = 0

        # Move right pointer through each character
        for r in range(len(s)):
            if s[r] in mp:
                # If character was seen before, move left past its previous occurrence
                l = max(mp[s[r]] + 1, l)

            # Update character's most recent index    
            mp[s[r]] = r
            res = max(res, r-l+1)  

        return res