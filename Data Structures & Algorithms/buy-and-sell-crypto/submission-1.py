class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        profit = 0
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
                j+=1
            else:
                diff = prices[j] - prices[i]
                if diff>profit:
                    profit = diff
                j+=1
        return profit  
        