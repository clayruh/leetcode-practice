# Smallest Even Multiple
def smallestEvenMultiple(n):
    # take in n, and find the smallest multiple of both 2 and n
    # sooo n ideally is a even number, which would return n
    if n%2 == 0:
        return n
    # if n is odd, then maybe 2 * n
    # can also assume that we don't need this if statement
    if n%2 != 0:
        return n*2