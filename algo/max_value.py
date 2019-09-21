def get_max(items):
    max_val = items[0]

    for i in range(1, len(items)):
        if items[i] > max_val:
            max_val = items[i]

    # end the for and return the max_val
    return max_val


myList = [1000]
print(get_max(myList))
