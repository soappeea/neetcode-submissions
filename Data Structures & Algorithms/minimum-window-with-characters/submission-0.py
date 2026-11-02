class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Expand right pointer until window contains all required chars from t
        # Then shrink from left to find the smallest valid substring
        if t == "":
            return ""

        # countT = required character frequencies from t
        # window = character frequencies in current substring of s
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have = 0 # Number of distinct chars meeting required frequency
        need = len(countT) # Number of distinct chars we need
        res = [-1,-1] # Start and end indices of smallest valid window
        resLen = float("infinity") # Length of smallest valid window found
        l = 0

        # Expand window by moving right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # If current char now meets its required count, increase have
            if c in countT and countT[c] == window[c]:
                have += 1
            
            # Window is valid when all required char frequencies are satisfied
            while have == need: 
                # Save current window if it's the smallest found
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1

                # Remove leftmost char to try making the window smaller
                window[s[l]] -= 1 

                # If removing it makes a required count too low, the window is no longer valid
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                # Move left pointer inward to shrink window
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        # Time: O(n + m) - Build frequency map of t, then each pointer moves through s once
        # Space: O(n + m) worst case - Frequency dictionaries and returned substring
        # n = len(s), m = len(t)    


        


        

        
        
