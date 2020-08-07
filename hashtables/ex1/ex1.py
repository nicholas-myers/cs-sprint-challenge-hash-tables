def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_index = {}
    # Your code here
    # GET ALL POSSIBLE COMBINATIONS
    # create the hash table
    if len(weights) == 1:
        return None
    indices = []
    for i, w in enumerate(weights):
        if w not in weight_index:
            weight_index[w] = i
        else:
            # print(w + w)
            if w + w == limit:
                indices.append(weight_index[w])
                indices.append(i)
    
    print(indices)
    return indices

# weights_1 = [9]
# answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
# weights_2 = [4, 4]
# get_indices_of_item_weights(weights_2, 2, 8)
# weights_3 = [4, 6, 10, 15, 16]
# get_indices_of_item_weights(weights_3, 5, 21)

weights_3 = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights_3, 5, 21)