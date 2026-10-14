class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [0] * n

        for i in range(n):
            prod = 1
            for z in range(n):
                if z == i:
                    continue
                
                prod *= nums[z]
            
            products[i] = prod
        
        return products