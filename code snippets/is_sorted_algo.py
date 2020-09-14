def is_sorted(itemlist):
    # using the all function
    # return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    # using the brute force method
    for i in range(0, len(itemlist)-1):
        if (itemlist[i] > itemlist[i+1]):
            return False
    return True


items1 = [6, 8, 19, 40, 23, 41, 50, 53, 56, 87]
items2 = [6, 21, 8, 19, 56, 299, 87, 41, 49, 53]

print(is_sorted(items1))
print(is_sorted(items2))
