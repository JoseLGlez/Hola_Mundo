def string_to_int(s):
    temp = str()
    try:
        string_to_number = int(eval(str(s)))
		if type(temp) == int:
            return temp
    
val = string_to_int('10')
print(val)
