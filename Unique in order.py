def unique_in_order(iterable):
    new_list = []
    i = 0
    for iter in iterable:
        if len(new_list) < 1 or not iter == new_list[len(new_list) - 1]:
            new_list.append(iter)
    return new_list