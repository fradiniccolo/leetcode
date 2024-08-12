class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buys = [range(prices[0], prices[0])]

        for price in prices[1:]:

            current_buy = buys[-1]

            if price > current_buy.stop:
                current_buy = range(current_buy.start, price)
                buys[-1] = current_buy

            elif price < current_buy.start:
                new_buy = range(price, price)
                buys.append(new_buy)

        def eval_profit(x): return x.stop - x.start
        best_buy = max(map(eval_profit, buys))
        return best_buy
