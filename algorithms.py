def quicksort(data, key):
    if len(data) <= 1:
        return data
    pivot = data[0]
    # Corrected comparison for descending order by key
    less = [item for item in data[1:] if item[key] > pivot[key]]
    greater = [item for item in data[1:] if item[key] <= pivot[key]]
    return quicksort(less, key) + [pivot] + quicksort(greater, key)