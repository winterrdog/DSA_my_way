def shell_sort(arr):
    '''
    Shell Sort
    Complexity: O(n^(3/2))
    '''
    arr_len = len(arr)

    def swap(i, j):
        arr[i], arr[j] = (arr[j], arr[i])

    # Calculate interval
    interval = 1
    while interval < arr_len // 3:
        interval = interval * 3 + 1

    while interval >= 1:
        for outer in range(interval, arr_len):
            # Select the value to be inserted
            inner = outer

            # Shift element towards right and moving down left the array, "interval"
            # times the array.
            while inner > (interval - 1) and arr[inner - interval] >= arr[inner]:
                # (inner - interval) means the preceding value, "interval" times back(
                # just like saying '2 times back')
                swap(inner, (inner - interval))

                # Move down the sublist interval times.
                inner -= interval

        # Calculate interval
        interval = (interval - 1) // 3

    return arr
