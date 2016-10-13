def binary_search(name, mylist):
    if mylist == []:
        raise ValueError("Not found")

    mid_index = len(mylist) / 2
    mid = mylist[mid_index]

    if name == mid:
        return mid
    elif name < mid:
        return binary_search(name, mylist[:mid_index])
    else:
        return binary_search(name, mylist[mid_index+1:])
