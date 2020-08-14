def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}

    for index in range(length):
        val = weights[index]
        target = limit - val

        if target not in weight_dict:
            weight_dict[val] = index
        else:
            target_index = weight_dict[target]
            return (index, target_index)
