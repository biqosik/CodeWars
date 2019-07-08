def create_phone_number(n):
    b = [str(item) for item in n]
    b = ''.join(b)
    return("({num}) {num1}-{num2}".format( num = b[0:3], num1 = b[3:6], num2 = b[6:10]))