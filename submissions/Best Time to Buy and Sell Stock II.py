class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        deltas = [
            next_price-curr_price 
            for curr_price, next_price 
            in zip(prices[:-1], prices[1:])
            ]
        gains = [delta for delta in deltas if delta > 0]
        return sum(gains)
