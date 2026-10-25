class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set for O(1) average lookup; order doesn't matter
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Check if num is the start of a sequence (no preceding number)
            if num - 1 not in numSet:
                length = 1
                # Keep counting while the next consecutive number exists
                while (num+length) in numSet:
                    length += 1
                     # Update longest sequence found
                longest = max(length, longest)
        return longest
        
