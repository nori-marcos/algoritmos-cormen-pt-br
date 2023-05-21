def recursive_linear_search(name, list_name, length, i):
    if i > length-1:
        return "not found"
    elif name == list_name[i]:
        return i
    else:
        return recursive_linear_search(name, list_name, length, i+1)


names = ['John', 'Paul', 'George', 'Ringo', 'Pete', 'Stuart']
print(recursive_linear_search("Marcos", names, len(names), 0))
