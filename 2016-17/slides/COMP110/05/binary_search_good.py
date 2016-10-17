def binary_search(name, mylist, start, end):
    if end <= start:
        raise ValueError("Not found")

    mid = (start + end) / 2
    mid_name = mylist[mid].name

    if name == mid_name:
        return mylist[mid]
    elif name < mid_name:
        return binary_search(name, mylist, start, mid)
    else:
        return binary_search(name, mylist, mid+1, end)
