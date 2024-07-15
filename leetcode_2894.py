def differenceOfSums(n: int, m: int):
    # num1 is the sum of all integers in range [1,n] not divisible by m
    # num2 is sum of all integers [1,n] divisible by m

    # for i in range(n):
    #     num1 = sum(i for i in n if n % m != 0)
    
    # for i in range(m):
    #     num2 = sum(i for i in n if n % m == 0)

    num1 = 0
    num2 = 0
    for i in range(1, n + 1):
        if i % m != 0:
            num1 += i
        else:
            num2 += i
    return num1 - num2
        
print(differenceOfSums(10,3))