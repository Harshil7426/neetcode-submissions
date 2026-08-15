class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_to_buy=float("inf")
        profit=0
        for i in range(len(prices)):
            best_to_buy=min(best_to_buy,prices[i])
            profit=max(profit,prices[i]-best_to_buy)
        return profit