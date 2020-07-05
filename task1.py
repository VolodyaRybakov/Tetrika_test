def search_pairs(array, k):
    results = set()
    for i in array:
        if i <= k:
            for j in array:
                if i + j == k:
                    results.add((i, j)) if i < j else results.add((j, i))
    return results


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

# Сложность алгоритма n^2
# Можно оптимизировать этот алгоритм, удалив повторяющиеся элементы, для этого можно преобразовать array в set, затем отсортировать сократившийся массив
# сортировака минимальная O(log(n)), плюс поиск пары для каждого числа O(n) (Оптимизация???) По итогу должно получиться около O(log(n))