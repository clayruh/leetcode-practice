def maxProfit(prices) -> int:
    # prices = [$, $$, $, $$$, $$]
    # return the maximum profit
    # max_profit = 0
    # # use two variables, one to find the lowest price, one to find the highest price
    # # loop through prices and replace either variable until the end of the array
    # buy_price = sell_price = prices[0]
    # for i in range(len(prices)):
    #     for j in range(i + 1,len(prices)):
    #         if prices[j] - prices[i] > max_profit:
    #             buy_price = prices[i]
    #             sell_price = prices[j]
    #             max_profit = sell_price - buy_price
    #             print(f'{buy_price} - {sell_price} {max_profit}')
    # return max(max_profit, buy_price - sell_price)

    # from Dean
    lowest_so_far = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        current_price = prices[i]
        if current_price > lowest_so_far:
            if current_price - lowest_so_far > profit:
                profit = current_price - lowest_so_far
            # profit = max(profit, current_price - lowest_so_far)
        if current_price < lowest_so_far:
            lowest_so_far = current_price
        # lowest_so_far = min(lowest_so_far, current_price)
    return profit

print(maxProfit([7,1,100,5,3,6,4]))