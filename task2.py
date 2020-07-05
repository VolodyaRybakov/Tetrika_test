def heapify(array, heap_size, root_index):
    largest = root_index
    left = (2 * root_index) + 1
    right = (2 * root_index) + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)


def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


def get_alphabet_sum(word):
    summa = 0
    for sym in word:
        summa += ord(sym.upper())-64

    return summa


array = []
with open('names.txt', 'r') as names:
    array = ','.join(names.readlines()).replace('"', '').split(',')

heap_sort(array)
result = 0
for i, name in enumerate(array):
    result += get_alphabet_sum(name)*i

print(result)

# Полученный ответ: 871529214
