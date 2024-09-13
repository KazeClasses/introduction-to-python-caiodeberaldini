def insertion_sort(unsorted_list: list[int]) -> list[int]:
    unsorted = True

    while(unsorted):
        swapped = False

        for i in range(len(unsorted_list)-1):
            if unsorted_list[i+1] < unsorted_list[i]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                swapped = True

        if not swapped:
            unsorted = False
    
    return unsorted_list