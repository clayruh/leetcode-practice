def finalValueAfterOperations(operations):
    # initialize x = 0
    # iterate through list 'operations' and interpret the strings
    x = 0
    for operation in operations:
        if operation == "--X" or operation == "X--":
            x -= 1
        else:
            x += 1
    return x

print(finalValueAfterOperations(["--X","X++","X++"]))