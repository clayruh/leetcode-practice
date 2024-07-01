data = ["Clae", "Dean", "Jasmine", "Dean", "Dean", "Clae", "Jasmine"]

def remove_dupes_1(array):
    return (set(array))

def remove_dupes_2(array):
    parsed_data = []
    for name in array:
        if name not in parsed_data:
            parsed_data.append(name)
    # print(parsed_data)
    return parsed_data

print(remove_dupes_1(data))

print(remove_dupes_2(data))