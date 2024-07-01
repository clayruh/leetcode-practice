# from dict bylines, grab each author in the array and return their names
# function must accept valid object format
# must remove invalid objects
# must output valid HTML string
# byline string must start with "By"
# Authors must be separated by a comma if more than 2
# last Author must be separated by an and
# Author must be wrapped by the style specified in the "block" parameter
# Assume support <em> and <strong> html tags

from data import bylines

def make_byline(bylines):
    style_dict = {
        "Bold": ['<strong>', '</strong>'],
        "Italics": ['<em>', '</em>'],
    }

    def make_sentence_case(string):
        string = string[0].upper() + string[1:].lower()
        return string

    array = bylines['authors']
    byline_string = "By "
    for i in range(len(array)):
        if 'firstName' in array[i] and 'lastName' in array[i]:
            if 'block' in array[i] and '__typename' in array[i]['block']:
            # if array[i]['block']: will cause keyError if 'block' doesn't exist in array[i]
                byline_string += style_dict[array[i]['block']['__typename']][0] + make_sentence_case(array[i]['firstName']) + " " + make_sentence_case(array[i]['lastName']) + style_dict[array[i]['block']['__typename']][1]
            else:
                byline_string += make_sentence_case(array[i]['firstName']) + " " + make_sentence_case(array[i]['lastName'])
            if len(array) >= 2:
                if i == len(array) - 2:
                    byline_string += ' and '
                    continue
                byline_string += ', '
    # this removes the last comma rather than writing an if statement looking at the "last object" in array
    return byline_string[:-2]

print(make_byline(bylines))