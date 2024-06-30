import string

def scoreOfString(s):
    # dict comprehension! {key: value for value, key in iterate(whatever produces the key, then value)}
    alphabet = {k: v for v, k in enumerate(string.ascii_lowercase, ord('a'))}
    # print(alphabet)

    # lol.. didn't even need to create the dict, can directly use ord() to find the value of a character

    score = 0
    # for loop through s, assign values to string looking thru our alphabet
    for i in range(0, len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
        print(score)
    # map out the algebra 
    return score

scoreOfString('zaz')