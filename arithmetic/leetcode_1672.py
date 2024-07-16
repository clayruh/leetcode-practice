def maximumWealth(accounts) -> int:
    # iterate through accounts and add up the sum of each array in accounts
    max_wealth = 0
    wealth = 0
    for account in accounts:
        for i in range(len(account)):
            wealth += account[i]
        if wealth > max_wealth:
            max_wealth = wealth
            wealth = 0
        else:
            wealth = 0
    return max_wealth
        
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))