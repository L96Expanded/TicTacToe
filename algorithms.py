# Algorithms we use for game logic. Linear search is also utilized, but because of the differences in
# implementation between its 2 necessary uses, we chose to not make it a seperate function
# AI algorithms are stored in the ai.py file

def quicksort(data, key):
    """
    Quicksort for sorting leaderboard and game history
    -Best Case: O(n log(n))
    -Worst Case: O(n^2)
    -Average Case: O(n log(n))
    """

    if len(data) <= 1:
        return data
    pivot = data[0]
    # Corrected comparison for descending order by key
    less = [item for item in data[1:] if item[key] > pivot[key]]
    greater = [item for item in data[1:] if item[key] <= pivot[key]]
    return quicksort(less, key) + [pivot] + quicksort(greater, key)