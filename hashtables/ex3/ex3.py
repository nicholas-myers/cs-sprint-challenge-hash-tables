

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    arr1 = {}
    dupes = {}
    trips = {}
    # Your code here
    # create a count for all numbers from all lists
    # get all the arrays
    # check all arrays for the number that is in all 3
    # check the len of the inner arrays
    result = []
    dupes_arr = []
    for num in arrays[0]:
        if num not in arr1:
            arr1[num] = 1
        else:
            arr1[num] += 1
    for num in arrays[1]:
        if num in arr1:
            dupes[num] = 1
            dupes_arr.append(num)
    if len(arrays) > 2:
        for num in arrays[2]:
            if num in arr1 and num in dupes:
                trips[num] = 1
        for key in trips.keys():
            result.append(int(key))
        return result
    else:
        return dupes_arr    
print(intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ]))
print(intersection([[1],[1],]))
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
    
