def argumentsLength(args):
    print(len(args))
    return len(args)

args = [{}, [1,2,3], False, "blahblah", 1000, []]
argumentsLength(args)

def checkArguments(args):
    # check args for lists and not count them 
    # return how many things in args that are NOT lists
    counter = 0
    for i in args:
        # is i a list?
        if type(i) != list:
            counter += 1
    return counter



# chicken = "chicken"

# def changeAnimal():
#     chicken = "bird"
#     print(chicken)
#     # don't have to return things, and if not return chicken, then chicken doesn't change to "bird" permanently outside of this function
#     return chicken

# chicken = changeAnimal()

# print(chicken)