

def quick_sort(array, n):
    if n <= 1:
        return array

    pivot = array[-1]
    array_left = []
    array_right = []

    for i in range(n-1):
        element = array[i]
        if element >= pivot:
            array_right.append(element)
        else:
            array_left.append(element)

    # by default is already sorted or empty
    sorted_left = array_left
    sorted_right = array_right

    n_left = len(array_left)
    n_right = len(array_right)
    if n_left > 1:
        sorted_left = quick_sort(array_left, n_left)
    if n_right > 1:
        sorted_right = quick_sort(array_right, n_right)

    sorted_left.extend([pivot])
    sorted_left.extend(sorted_right)
    return sorted_left

def is_major(element, comparison):
    len_element = len(element)
    len_comparison = len(comparison)

    diff = abs(len_comparison-len_element)
    
    if len_comparison > len_element:
        element = "0"*diff + element
    elif len_comparison < len_element:
        comparison = "0"*diff + comparison 

    max_len = max(len_element, len_comparison)

    i = max_len - 1
    while i >= 0:
        if element[i] > comparison[i]:
            return True
        elif element[i] < comparison[i]:
            return False
        # if are equals continue with other digits...
        i -= 1
        
    # then, are equal
    return True

def quick_sort_special(array, n):
    if n <= 1:
        return array

    pivot = array[-1]
    array_left = []
    array_right = []

    for i in range(n-1):
        element = array[i]
        if is_major(str(element), str(pivot)):
            array_right.append(element)
        else:
            array_left.append(element)

    # by default is already sorted or empty
    sorted_left = array_left
    sorted_right = array_right

    n_left = len(array_left)
    n_right = len(array_right)
    if n_left > 1:
        sorted_left = quick_sort_special(array_left, n_left)
    if n_right > 1:
        sorted_right = quick_sort_special(array_right, n_right)

    sorted_left.extend([pivot])
    sorted_left.extend(sorted_right)
    return sorted_left

 

print(quick_sort_special([1, 10, 20, 33, 13, 60, 92, 100, 21], 9))