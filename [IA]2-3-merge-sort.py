# só junta duas listas ordenadas numa única lista ordenada
def merge(array: list, start_index: int, middle_index: int, end_index: int):
    n1: int = middle_index - start_index + 1  # tamanho do subarray da esquerda [p ... q]
    n2: int = end_index - middle_index  # tamanho do subarray da direita [q + 1 ... r]
    left: list = [0] * (n1 + 1)  # cria um array de tamanho n1 + 1
    right: list = [0] * (n2 + 1)  # cria um array de tamanho n2 + 1
    # em ambos arrays, foi criado uma posição a mais para armazenar a posição sentinela
    # a carta sentinela é o fim da pilha de cartas
    for i in range(0, n1):  # copia os elementos da esquerda para o array left
        left[i] = array[start_index + i]
    for j in range(0, n2):  # copia os elementos da direita para o array right
        right[j] = array[(middle_index + 1) + j]
    left[n1] = float("inf")  # a carta sentinela é o fim da pilha de cartas
    right[n2] = float("inf")  # a carta sentinela é o fim da pilha de cartas
    i: int = 0  # i é o índice da carta atual da esquerda
    j: int = 0  # j é o índice da carta atual da direita
    # aqui o array original é organizado
    # itera sobre o array original, da posição p até a posição r + 1
    for k in range(start_index, end_index + 1):  # k é o índice da carta atual do array original
        left_card: int = left[i]  # left_card é a carta atual da esquerda
        right_card: int = right[j]  # right_card é a carta atual da direita
        if left_card <= right_card:  # se a carta da esquerda for menor ou igual à carta da direita
            array[k] = left[i]  # a carta da esquerda vai para a posição k do array original
            i += 1  # i é incrementado
        else:  # se a carta da direita for menor que a carta da esquerda
            array[k] = right_card  # a carta da direita vai para a posição k do array original
            j += 1  # j é incrementado


# quebra o array em duas partes até que cada parte tenha apenas um elemento (caso trivial)
def merge_sort(array: list, p, r):
    if p < r:
        q: int = (p + r) // 2  # q é o índice do meio do array
        print(f"p: {p}, q: {q}, r: {r}")
        merge_sort(array, p, q)  # ordena a primeira metade do array
        merge_sort(array, q + 1, r)  # ordena a segunda metade do array
        merge(array, p, q, r)  # junta as duas metades ordenadas


array: list = [5, 2, 4, 6, 1, 3]

print(merge_sort(array, 0, 5))
print(array)
