from string import digits, ascii_letters

valid_values = list(digits + ascii_letters)
print(valid_values)
e = '№8*9;6::5??0**5"9ggg;9$9@1&0AAAA'
e = list(e)
print(e)
tel = list(filter(lambda x: x in valid_values, e))
print(tel)
