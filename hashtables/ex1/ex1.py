def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create cache
    cache = {}

    # make the keys the weights and the values the indices
    for i in range(len(weights)):
        cache[weights[i]] = i
    # print(cache)
    # for each weight find the difference
    # if it matches, return the indices 
    for i in range(len(weights)):
        diff = limit-weights[i]
        if diff in cache:
            return (max(i, cache[diff]), min(i, cache[diff]))

    return None

# ouput should be [3,1]
weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))
