# U P E R

# U - Understand
# Package with a weight limit `limit`
# List `weights` of item weights

# Function should find two items who's sum of weights
# equals the weight limit.

# The higher valued index should be placed in the 0th index of output.
# Lower should be in the 1st index of output.
# If such a pair doesn't exist, return `None`.

# Input: A list of weights.
# Output: Tuple e.x.: (zero, one)

# P - Plan
# Our function needs a dict to store the weight inputs as keys
# and each weight list's indexs as it's value.
# We can then look through the hash table for any
# entries the limit - weight and that is how we'll
# find our two items whos weights equal the limit.


# E - Execute

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}

    for key in range(length):
        weight = weights[key]
        target = limit - weight

        if target not in weight_dict:
            weight_dict[weight] = key
        else:
            index = weight_dict[target]
            return (key, index)

# R - Reflect
# I used a dict to store weight inputs as keys,
# and set the weight's list index as the value pair.
# Trying to get better at naming variables.
