def maxProfit(prices) -> int:
    # prices = [$, $$, $, $$$, $$]
    # return the maximum profit
    max_profit = 0
    # use two variables, one to find the lowest price, one to find the highest price
    # loop through prices and replace either variable until the end of the array
    buy_price = sell_price = prices[0]
    for i in range(len(prices)):
        for j in range(i + 1,len(prices)):
            if prices[j] - prices[i] > max_profit:
                buy_price = prices[i]
                sell_price = prices[j]
                max_profit = sell_price - buy_price
                print(f'{buy_price} - {sell_price} {max_profit}')
            else:
                continue
    return max(max_profit, buy_price - sell_price)

print(maxProfit([7,1,5,3,6,4]))