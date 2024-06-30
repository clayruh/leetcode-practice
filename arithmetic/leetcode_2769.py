def theMaximumAchievableX(num , t):
    # what is the greatest number, that either + or - 1, will equal num
    # and can only be done 't' times 
    
    # so, aka ref# is going to be num + 1 * t then to get max_num, we take that ref# + 1 * t
    # ie. if num = 3, t = 2 | 3 + 1 * 2 = 5 rev# = 5 | max_num = 5 + 1 * 2 = 7
    print((num + 1 * t) + 1 * t)
    return (num + 1 * t) + 1 * t

theMaximumAchievableX(4, 1)