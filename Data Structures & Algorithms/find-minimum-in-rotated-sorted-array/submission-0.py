class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = nums[0]

        while l <= r:
            # if array is sorted
            if nums[l] < nums[r]:
                lowest = min(lowest, nums[l]) 
                break
            
            # find middle index and save its value if it's the smallest so far
            mid = l + (r-l)//2
            lowest = min(lowest, nums[mid])
            if nums[mid] >= nums[l]:
                # left half is sorted (no rotation point between l and mid)
                # minimum is either already saved or somewhere to the right
                # skip left half and search right
                l = mid + 1
            else:
                # rotation point in left half
                # Example: [6, 7, 0, 1] where mid points to 1
                # minimum is at mid or somewhere to its left
                # already checked mid, so search before it
                r = mid - 1

        
        return lowest