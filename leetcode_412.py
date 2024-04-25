def fizzBuzz(n):
    # n is an integer
    # starting at index 1,
    # for i in range(n):
    # return FizzBuzz if i % 3 and 5 == 0
    # return Fizz if i % 3 == 0
    # return Buzz if i % 5 == 0
    # else return "i"

    answer = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
            # continue makes is so that it exists the loop rather than fulfill the following conditions
            continue
        if i % 3 == 0:
            answer.append("Fizz")
        if i % 5 == 0:
            answer.append("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            answer.append(str(i))
    print(answer)
    return answer

fizzBuzz(15)