class Solution:
    '''
    given prices where prices[i] is the price of the coin for ith day

    one day to buy, one day to sell

    return max and choice to not make transactions

    Input: prices = [10,1,5,6,7,1]

    Buy ? 10 no sell 10? no you havent bought anything

    buy 1? sure

    sell 5? profit would be 4

    sell 6 profit would be 5

    sell 7 profit would be 6

    sell 1 get 0

    keep track of max profit

    if current > max_profit:
        max_profit = current

    Output: 6

    '''
    def maxProfit(self, prices: List[int]) -> int:

        current = prices[0]
        max_profit = 0
        for n in prices:
            #BUY
            if n < current:
                current = n
            
            max_profit = max(max_profit, n - current )
            
        return max_profit

        