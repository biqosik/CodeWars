import math
def decomp(n):
    factory = math.factorial(n)
    i = 2
    alls = ""
    factors = []
    xfactors = []
    while i * i <= factory:
        if factory % i:
            i += 1
        else:
            factory //= i
            factors.append(i)
            if i not in xfactors:
                xfactors.append(i)
    if factory > 1:
        factors.append(factory)
        xfactors.append(factory)
    for ie in xfactors:
        if factors.count(ie) > 1:
            alls += str(ie) + "^" + str(factors.count(ie)) + " * "
        else:
            if xfactors[-1] == ie:
                return alls + str(ie)
            alls +=str(ie) + " * "

print(decomp(int(input("Enter your input: "))))
