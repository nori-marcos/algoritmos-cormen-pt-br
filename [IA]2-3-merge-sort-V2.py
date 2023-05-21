
# funcao de apoio merge (só funciona para duas pilhas ordenadas)
# junta duas pilhas de cartas ordenadas numa única pilha ordenada
def merge(left_list, right_list):
    combined_list = []
    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):  # enquanto houver cartas nas duas pilhas
        left_card = left_list[i]  # carta atual da pilha da esquerda
        right_card = right_list[j]  # carta atual da pilha da direita
        if left_card <= right_card:
            combined_list.append(left_card)
            i += 1
        else:
            combined_list.append(right_card)
            j += 1

    while i < len(left_list):  # enquanto houver cartas na pilha da esquerda
        combined_list.append(left_list[i])
        i += 1
    while j < len(right_list):  # enquanto houver cartas na pilha da direita
        combined_list.append(right_list[j])
        j += 1

    return combined_list


# merge sort
def merge_sort(array):
    if len(array) <= 1:
        # #1 caso base: merge sort não precisa ordenar um array com apenas um elemento. Ele já está ordenado.
        return array
    else:  # quebrar o array em duas partes até que cada parte tenha apenas um elemento (caso trivial)
        middle_index = len(array) // 2
        left_list = merge_sort(array[:middle_index])  # ordena a primeira metade do array
        right_list = merge_sort(array[middle_index:])  # ordena a segunda metade do array
        #  #2 após chegar no caso trivial/base, left e right tem um elemento cada
        #  #3 merge vai juntar as duas metades com elemento, formando uma lista com dois elementos
        return merge(left_list, right_list)  # junta as duas metades ordenadas

