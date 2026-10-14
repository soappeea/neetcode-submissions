class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arranged_s = sorted(s)
        arranged_t = sorted(t)
        if set(s) != set(t) or len(s) != len(t):
            return False
        
        for i in range(len(arranged_s)):
            if arranged_s[i] != arranged_t[i]:
                return False
        
        return True
        
            
