class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) average lookup and remove duplicates
        numSet = set(nums)
        longest = 0

        for num in numSet:
    # Check if num is the start of a sequence (no preceding number)
            if (num - 1) not in numSet:
                length = 1
            # Count consecutive numbers until the sequence ends
                while (num + length) in numSet:
                    length += 1
                # Update longest sequence found
                longest = max(length, longest)

        return longest

# Time: O(n) - Each sequence is traversed only from its starting number
# Space: O(n) - Set stores up to n unique numbers   