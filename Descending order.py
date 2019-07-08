def Descending_Order(num):
    new_list = []
    for a in str(num):
        new_list.append(int(a))
    new_list.sort(reverse=True)
    return int("".join( str(x) for x in new_list ))