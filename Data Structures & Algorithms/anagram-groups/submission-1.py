class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char)-ord('a')] += 1
            
            key = tuple(count)
                
            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        
        return list(groups.values())

        # Create dictionary to group anagrams
        # Loop through each word and count character frequencies using ord()
        # Convert frequency list to tuple so it can be a dictionary key
        # Words with identical frequencies share the same key
        # If key doesn't exist, initialize an empty list
        # Append original word to its corresponding group
        # Return dictionary values as a list of lists
        