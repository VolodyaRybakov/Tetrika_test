def search_pairs(array, k):
    array = sorted(array)
    results = set()
    for i, val1 in enumerate(array):
        if val1 > k:
            break
        for val2 in array[i+1:]:
            if val1 + val2 == k:
                results.add((val1, val2)) if val1 < val2 else results.add(
                    (val2, val1))
                break

    return list(results)


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2, 0], 6))

# Сложность алгоритма n^2
