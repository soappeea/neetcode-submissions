class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            if key not in groups: # check if the key is in dict
                groups[key] = []  # initialize list if not yet added
            groups[key].append(s)

        return list(groups.values())        

# Create a dictionary with the current 
# Go through all the strings, update count based on which 
# char is in the current string. 
# tuple(count) in line 9 is the key(index), add the string to that index
# once all done, return the grouped anagrams