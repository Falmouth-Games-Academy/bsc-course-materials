def binary_search(name, mylist, start, end):
    if end <= start:
        raise ValueError("Not found")

    mid_index = (start + end) / 2
    mid = mylist[mid_index]

    if name == mid:
        return mid
    elif name < mid:
        return binary_search(name, mylist, start, mid)
    else:
        return binary_search(name, mylist, mid+1, end)
