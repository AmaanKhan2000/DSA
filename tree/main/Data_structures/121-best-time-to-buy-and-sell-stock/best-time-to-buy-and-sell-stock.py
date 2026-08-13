class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        temp = 0
        for i in range(len(prices)-1):
            j=i+1
            while j<len(prices):
                if prices[j]<=prices[i]:
                    break
                else:
                    temp = prices[j]-prices[i]
                    j+=1
                maxi = max(temp,maxi)
        return maxi        




        