# U P E R

# U - Understand

# We are trying to find the intersection between
# multiple arrays of numbers.
# DICT or hashtables ONLY.
# We are given a list of lists.

# Input: A list of lists of integers.
# Output: The integers that exist in all lists.

# P - Plan
# We need a dict to store our arrays in
# Then we can compare the integers in the arrays

# E - Execute

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
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


# R - Reflect
