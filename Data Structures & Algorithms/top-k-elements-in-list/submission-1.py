class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        highest_val = max(freq.values())


        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]  # iterate over freq dict, x is each elem, use freq values to sort, reverse to have highest freq first, return first k nums
            
