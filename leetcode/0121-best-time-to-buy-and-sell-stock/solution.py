class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price - min_price > max_profit:
                max_profit = price - min_price
            if price < min_price:
                min_price = price

        return max_profit

            # if prices[left] == p_left and not left_find:
            #     left_find = True
            
            # if prices[right] == p_right and left_find:
            #     right_find = True
            # else: 
            #     ...
            # p_left = prices[left]
            # p_rigth = prices[right]
            # if right > 0:
            #     right -= 1

            
