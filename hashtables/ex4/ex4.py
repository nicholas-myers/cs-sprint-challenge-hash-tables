
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    pos = {}
    neg = {}
    # Your code here
    result = []
    for num in a:
        if abs(num) not in neg:
            neg[abs(num)] = num
        elif abs(num) not in pos:
                pos[abs(num)] = 1
    for key in pos.keys():
        result.append(key)

    return result
# print(has_negatives([1,2,3]))

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([1,2,3]))
