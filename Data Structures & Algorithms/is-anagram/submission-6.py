class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        return countS == countT

        # unequal length then cannot be anagram
        # add count to specific char that shows up
        # compare if chars show up same amount of times in each string
        # O(n) since loop through