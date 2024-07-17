def maxProfit(prices) -> int:
    # prices = [$, $$, $, $$$, $$]
    # return the maximum profit
    # max_profit = 0
    # use two variables, one to find the lowest price, one to find the highest price
    # loop through prices and replace either variable until the end of the array
    # buy_price = sell_price = prices[0]
    # for i in range(len(prices)):
    #     for j in range(i + 1,len(prices)):
    #         if prices[j] - prices[i] > max_profit:
    #             buy_price = prices[i]
    #             sell_price = prices[j]
    #             max_profit = sell_price - buy_price
    #             print(f'{buy_price} - {sell_price} {max_profit}')
    #         else:
    #             continue
    # return max(max_profit, buy_price - sell_price)


    # I'm not sure why this works, it's from leetcode
    # left = 0 #Buy
    # right = 1 #Sell
    # max_profit = 0
    # while right < len(prices):
    #     current_profit = prices[right] - prices[left]
    #     if prices[left] < prices[right]:
    #         max_profit = max(current_profit, max_profit)
    #     else:
    #         left = right # why do we move the pointers?? what if a higher sell price was after this?
    #     right += 1
    # return max_profit

    # from Dean
    lowest_so_far = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > lowest_so_far:
            profit = max(profit, prices[i] - lowest_so_far)
        lowest_so_far = min(lowest_so_far, prices[i])
    return profit

print(maxProfit([7,1,5,3,6,4]))