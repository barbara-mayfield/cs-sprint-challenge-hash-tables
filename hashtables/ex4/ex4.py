def has_negatives(a):
    """
    YOUR CODE HERE
    """
    ht = {}
    result = []

    for x in a:
        if x != 0:
            ht[x] = 1
            if -x in ht:
                result.append(abs(x))  # abs returns absolute value of a num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
