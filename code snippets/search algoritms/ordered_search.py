items = [6, 21, 32, 33, 59, 89, 99, 243]


def binarysearch(item, itemlist):
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = len(itemlist) - 1

    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # if item is found, return the index
        if itemlist[midPt] == item:
            return midPt
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(32, items))
print(binarysearch(89, items))
print(binarysearch(270, items))
