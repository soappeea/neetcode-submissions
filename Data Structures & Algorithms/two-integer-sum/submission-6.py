class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []

        # Dictionary lookup is O(1) on average
        # Store previously visited numbers: value -> index
        # Use enumerate() to get both index and value
        # Calculate complement = target - num
        # If complement is in seen, return both indices
        # Otherwise, store num -> index and continue