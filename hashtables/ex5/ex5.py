# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    only_files = {}
    dupes = {}
    for f in files:
        if f.find("/") == -1:
            only_files[f] = f
        lonely = f.split("/")
        last = len(lonely) - 1
        # print(lonely)
        if lonely[last] not in only_files:
            only_files[lonely[last]] = f
        else:
            dupes[lonely[last]] = f
    # print(only_files)
    for q in queries:
        if q in only_files:
            result.append(only_files[q])
        if q in dupes:
            result.append(dupes[q])
            
        
    
    # print(files)
    # print(queries)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
    # files = []
    # for i in range(500000):
    #         files.append(f"/dir{i}/file{i}")

    # for i in range(500000):
    #         files.append(f"/dir{i}/dirb{i}/file{i}")

    # queries = []

    # for i in range(1000000):
    #     queries.append(f"nofile{i}")

    #     queries += [
    #         "file3490",
    #         "file256",
    #         "file999999",
    #         "file8192"
    #     ]
    # print(finder(files, queries))
        
