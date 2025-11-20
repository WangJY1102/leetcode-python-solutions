from typing import List

class Solution:
    def maxPrifit(self, prices: List[int]) -> int:
        """买卖股票最佳时机
        暴力解法，时间复杂度太高
        每次都假设是今天卖出，求今天卖最大多少利润。然后求今天之前的历史最低点minprices。
        而这个历史最低点并不需要额外遍历，而是每天考虑的时候顺带记录的。
        """
        for i, prices in enumerate(prices):
            if i == 0:
                maxprofit = 0
                minprices = prices
            maxprofit = max(prices - minprices, maxprofit)
            minprices = min(prices, minprices)
        return maxprofit

if __name__ == "__main__":
    prices = list(map(int, input("请输入价格数组（空格分隔）：").split()))
    maxprofit = Solution().maxPrifit(prices)
    print("可能的最大利润：", maxprofit)

