def dynamicArray(n, queries):
    # Initialize an empty 2-dimensional array with n empty arrays
    arr = [[] for _ in range(n)]

    # Initialize the last_answer variable to 0
    last_answer = 0

    # Create an empty list to store the answers
    answers = []

    # Iterate over each query in the queries list
    for query in queries:
        # Split the query string into three parts: q, x, and y
        q, x, y = map(int, query.split())

        # Calculate the index in the arr list based on the XOR operation and modulo operation
        idx = (x ^ last_answer) % n

        # If q is 1, it's a type 1 query
        if q == 1:
            # Append the integer y to the corresponding array in arr
            arr[idx].append(y)
        
        # If q is 2, it's a type 2 query
        elif q == 2:
            # Get the size of the array at the corresponding index
            size = len(arr[idx])

            # Calculate the new value of last_answer based on the value of y and the size of the array
            last_answer = arr[idx][y % size]

            # Append the new value of last_answer to the answers list
            answers.append(last_answer)

    # Return the list of answers
    return answers
