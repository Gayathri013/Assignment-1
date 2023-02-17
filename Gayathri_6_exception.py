int_val = 8
str_val = "Hello"
try:
    result = int_val + str_val
    # trying to add integer with string
    print(result)
except Exception:
    print("msg : You can\'t add int to string")
    # if exception is caught in try block above msg is displayed 
