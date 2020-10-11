# U P E R

# U - Understand
# We need to solve this problem with a hash table.

# Input: An unordered list of positive and negative integers.
# Output: Positive numbers that have corresponding negative numbers.

# P - Plan
# E - Execute

def has_negatives(integers):
    """
    YOUR CODE HERE
    """
    table = {}
    result = []

    for integer in integers:
        if integer != 0:
            table[integer] = 1
            if -integer in table:
                # abs returns absolute value of a num
                result.append(abs(integer))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

# R - Reflect
