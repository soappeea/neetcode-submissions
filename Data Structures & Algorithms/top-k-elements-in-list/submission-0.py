class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # if n doesn't already exist in hashmap add 0

        for n, c in count.items(): #return every single key val pair added to dict
            freq[c].append(n) # val n occurs c num of times

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                # if n is non-empty then add it to result
                res.append(n)
                if len(res) == k:
                    return res
        