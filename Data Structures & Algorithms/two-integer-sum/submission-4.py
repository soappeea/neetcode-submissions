class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []

        # searching in dict is O(1)
        # dict for keeping count of #'s visited and their index
        # loop using enumerate since using both index and val
        # return indexes if complement was in seen dict
        # otherwise add to seen dict and continue till find 