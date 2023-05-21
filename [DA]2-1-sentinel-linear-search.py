def find_name(name, list_name):
    length = len(list_name)
    # sentinela é o último elemento da lista "caixa de livro vazia"
    names_with_sentinel = list_name + [name]
    length_with_sentinel = length + 1
    i = 0
    # enquanto o nome atual for diferente do nome procurado, incrementa i
    while names_with_sentinel[i] != name:
        i += 1
    if i == length_with_sentinel - 1:
        return "not found"
    else:
        return f"It is in {i}"


names = ['John', 'Paul', 'George', 'Ringo', 'Pete', 'Stuart']
print(find_name("Paul", names))
