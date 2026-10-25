class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort numbers to use two pointers and handle duplicates
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Stop if smallest remaining number is positive (sum cannot be 0)
            if a > 0:
                break

            # Skip duplicate first numbers to avoid repeated triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Initialize two pointers after the current number
            l, r = i + 1, len(nums) - 1

            while l < r:
                # Calculate sum of three numbers
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    # Sum too large, move right pointer left to decrease sum
                    r -= 1

                elif threeSum < 0:
                    # Sum too small, move left pointer right to increase sum
                    l += 1

                else:
                    # Valid triplet found, add to result
                    res.append([a, nums[l], nums[r]])

                    # Move both pointers to search for another triplet
                    r -= 1
                    l += 1

                    # Skip duplicate left values to avoid repeated triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

        # Time: O(n²) - Outer loop + two-pointer search
        # Space: O(n) worst case for Python sorting, excluding output
