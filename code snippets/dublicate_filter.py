def no_dublicate(items):
    # create a hashtable to perform a filter
    data = dict()

    # loop over each item and add to the hashtable
    for item in items:
        data[item] = 0

    # create a set from the resulting keys in the hashtable
    return set(data.keys())

# test

# define a set of items that we want to reduce duplicates
myList = ["apple", "pear", "orange", "banana", "apple",
          "orange", "apple", "pear", "banana", "orange",
          "apple", "kiwi", "pear", "apple", "orange"]

print(no_dublicate(myList))
