def order_weight(strng):
    newer = sorted(strng.split(' '))
    newest = sorted(newer, key=foes)
    return ' '.join(newest)


def foes(n):
    return sum([int(item) for item in n])
print("Your lane: ", end="")
print(order_weight(input()))
