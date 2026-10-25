class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        # Two pointers: l = buy day (lowest price), r = sell day
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                # Selling price > buying price, calculate potential profit
                # Update maximum profit if current trade is better
                maxP = max(maxP, prices[r] - prices[l])
            else:
                # Found a cheaper buying price, update buy day
                l = r

            # Move to next possible selling day
            r += 1

        return maxP

    # Time: O(n) - Each price is visited once
    # Space: O(1) - Only two pointers and max profit variable