def differenceOfSums(n: int, m: int):
    # num1 is the sum of all integers in range [1,n] not divisible by m
    # num2 is sum of all integers [1,n] divisible by m
    # num1_arr = []
    # num2_arr = []
    # for i in range(n+1):
    #     if i % m != 0:
    #         num1_arr.append(i) 
    #     if i % m == 0:
    #         num2_arr.append(i)
    # num1 = sum(n for n in num1_arr)
    # num2 = sum(n for n in num2_arr)
    # print(num1_arr,num2_arr)

    num1 = 0
    num2 = 0
    for i in range(1, n + 1):
        if i % m != 0:
            num1 += i
        else:
            num2 += i
    return num1 - num2
        
print(differenceOfSums(5,6))