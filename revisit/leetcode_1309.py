import string

def freqAlphabets(s):
    # a for loop where '1'-'9' maps to 'a'-'i' and '10#' - '26#' maps to 'j' - 'z'

    # assuming s is a mix of integers and integers w #
    # could loop through s backwards and have a condition to account for the two digits after the '#'
    # ie, toggle seen_a_pound = False, and once we do, then we have a statement to append the following 2 digits grouped

    # I first tried to have a boolean toggle, but a counter somehow works better as brute force
    seen_a_pound_counter = 0
    pound_number = ""
    s_as_list = []
    output = ""
    for c in s[::-1]:
        if c != '#' and seen_a_pound_counter == 0:
            s_as_list.append(c)
        if c == '#':
            seen_a_pound_counter += 1
            pound_number += '#'
            print(f'counter: {seen_a_pound_counter} c: ' + c)
        if c != '#' and seen_a_pound_counter == 1:
            seen_a_pound_counter += 1
            pound_number += c
            print(f'counter: {seen_a_pound_counter} c: ' + c)
            continue
        if c != '#' and seen_a_pound_counter == 2:
            pound_number += c
            s_as_list.append(pound_number[::-1])
            seen_a_pound_counter = 0
            pound_number = ""
            print(f'counter: {seen_a_pound_counter} c: ' + c)
            print(pound_number[::-1])
            print(s_as_list)

    alphabet = string.ascii_lowercase
    dictionary = {}
    for i in range(26):
        if i < 9:
            dictionary[str(i + 1)] = alphabet[i]
        if i >= 9:
            dictionary[str(i + 1) + '#'] = alphabet[i]
    print(dictionary)
    # for num in s_as_list:
    #     if num == '1':
    #         output += 'a'
    #     if num == '2':
    #         output += 'b'
    #     if num == '3':
    #         output += 'c'
    #     if num == '4':
    #         output += 'd'
    #     if num == '5':
    #         output += 'e'
    #     if num == '6':
    #         output += 'f'
    #     if num == '7':
    #         output += 'g'
    #     if num == '8':
    #         output += 'h'
    #     if num == '9':
    #         output += 'i'

    #     if num == '10#':
    #         output += 'j'
    #     if num == '11#':
    #         output += 'k'
    #     if num == '12#':
    #         output += 'l'
    #     if num == '13#':
    #         output += 'm'
    #     if num == '14#':
    #         output += 'n'
    #     if num == '15#':
    #         output += 'o'
    #     if num == '16#':
    #         output += 'p'
    #     if num == '17#':
    #         output += 'q'
    #     if num == '18#':
    #         output += 'r'
    #     if num == '19#':
    #         output += 's'
    #     if num == '20#':
    #         output += 't'
    #     if num == '21#':
    #         output += 'u'
    #     if num == '22#':
    #         output += 'v'
    #     if num == '23#':
    #         output += 'w'
    #     if num == '24#':
    #         output += 'x'
    #     if num == '25#':
    #         output += 'y'
    #     if num == '26#':
    #         output += 'z'
        
    print(output[::-1])


    # if seen_a_pound == False, then we can interpret the string into a a-i and append that into a list

    # eventually we loop through the chopped up s_as_list and interpret into letters
    return output[::-1]

freqAlphabets("10#11#12")