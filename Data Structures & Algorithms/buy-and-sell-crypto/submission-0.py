class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_at = prices[0]
        profit = 0

        for price in prices:
            if price < buy_at:
                buy_at = price
            profit = max(profit, price - buy_at)

        return profit
