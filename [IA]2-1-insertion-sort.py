# organizando cartas de uma mão
# insertion sort

def insertion_sort(array):
    for j in range(1, len(array)):  # j é o índice da carta atual. comecamos analisando da segunda carta: indice 1
        key = array[j]  # key é a carta atual
        i = j - 1  # i é o índice da carta anterior
        while i >= 0 and array[i] > key:  # enquanto a carta anterior for maior que a atual
            array[i + 1] = array[i]  # a carta anterior vai para a posição da carta atual
            i -= 1  # i é decrementado
        array[i + 1] = key  # a carta atual vai para a posição da carta anterior
    return array


print(insertion_sort([5, 2, 4, 6, 1, 3]))
