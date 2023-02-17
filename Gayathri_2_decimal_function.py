def the_decimal(val):
    if val == int(val):
        # checks whether the value is integer
        print("INTEGER")
    else:
        val = str(val).split(".")[1]
        # takes decimal value as string
        print("Decimal value of required string is",int(val))

# another way
# def the_decimal(val):
#     if val == int(val):
#         print("INTEGER")
#     else:
#         count=len(str(val).split(".")[1])
#         decimal_values = 1
#         for i in range(0,count):
#             decimal_values *= 10

#         decimal = val - int(val)
#         print(int(decimal*decimal_values))


decimal_number = float(input("Enter a number:"))
the_decimal(decimal_number)