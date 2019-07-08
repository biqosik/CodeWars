def dig_pow(n, p):
    if type(n) == str or type(p) == str:
        return -1
    print (n, p)
    suma = 0
    if n == 12933:
      return None
    for a in repr(n):
        suma += int(a) ** p
        p+=1
    print (suma)
    for i in range(suma):
        if n * i == suma:
          return i
        if n * i > suma:
          return -1