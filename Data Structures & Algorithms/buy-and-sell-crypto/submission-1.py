class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_to_buy=float("inf")
        profit=0
        for i in prices:
            best_to_buy=min(best_to_buy,i)
            profit=max(profit,i-best_to_buy)
        return profit