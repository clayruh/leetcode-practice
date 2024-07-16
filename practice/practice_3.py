def parentheses(string):
    # accept a string filled with () and determine if string is valid
    # implement a stack concept to track opening and closing parentheses
    stack = []
    for char in string:
        if char == ")" and len(stack) == 0: 
            return False
        if char == ")":
            stack.pop()
        if char == "(":
            stack.append(char)
            
    return len(stack) == 0

print(parentheses("("))