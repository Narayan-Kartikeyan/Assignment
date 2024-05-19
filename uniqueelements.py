def find_unique_elements(arr):
    unique_elements = []
    for num in arr:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements