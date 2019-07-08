import re
def increment_string(strng):
    number = re.findall(r'\d+', strng)
    if number:
        s_number = number[-1]
        strng = strng.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return strng + '0' * (len(s_number) - len(number)) + number
    return strng + '1'