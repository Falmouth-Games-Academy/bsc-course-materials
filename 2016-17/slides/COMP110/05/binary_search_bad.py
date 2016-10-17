def binary_search(name, mylist):
    if mylist == []:
        raise ValueError("Not found")

    mid = len(mylist) / 2
    mid_name = mylist[mid_index].name

    if name == mid_name:
        return mid
    elif name < mid_name:
        return binary_search(name, mylist[:mid])
    else:
        return binary_search(name, mylist[mid+1:])
