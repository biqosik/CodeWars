def find_it(seq):
    for i in seq:
        x = seq.count(i)
        if (x % 2 ) == 1:
            return i