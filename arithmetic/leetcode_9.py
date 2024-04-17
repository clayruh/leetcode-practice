def isPalindrome(x):
    if x < 0:
        print("false")
        return False
    reverse_number_as_list = helperFunction(x) #[7,2,1]
    if reverse_number_as_list == reverse_number_as_list[::-1]:
        print("true")
        return True
    else:
        print("false")
        return False
    
        

def helperFunction(number):
    # takes in a single number and returns a list of the digits
    
    number_as_list = []
    x = number
    while x > 0:
        # creating new variables to keep track of the digit
        a = x % 10
        number_as_list.append(a)
        x = x//10
    print(number_as_list)
    return number_as_list

isPalindrome(121)


    # x = 127
    # a = x % 10 = 7 
    # number_as_list.append(a)
    # x = x//10 = 12 #reassignment
    # b = x % 10 = 2
    # x = x//10 = 1 #reassignment
    # c = x % 10 = 1
    # x = x//10 = 1 #reassignment
    # d = x % 10 = 0