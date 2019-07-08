def triple_double(num1, num2):
    if num1 == '':
        return 0
    new_list = [10]
    i = 0
    for n in str(num1):
        new_list.append(n)
        if i == 2:
            i = 0
            break
        elif n == new_list[-2]:
            i+=1
    n = new_list[-2]
    for m in str(num2):
        if m == n:
            i+=1
            if i == 2:
                return 1
        elif m != n:
            i==0
    return 0