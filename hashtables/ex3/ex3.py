def intersection(arrays):
    """
    YOUR CODE HERE
    """
    arr_table = {}

    for a in arrays:
        for x in a:
            if x in arr_table:
                arr_table[x] += 1
            else:
                arr_table[x] = 1

    result = [x[0] for x in arr_table.items() if x[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
