def the_decimal(val):
    """
    This function the decimal value of the given number , 
    if the demial value is zero then it prints integer

    params :-
    val : stores user given float value

    Returns :-
    string : if the contidion satisfies returns string "INTEGER"

    """
    if val == int(val):
        return "INTEGER"
    
number = 3.6
decimal_number = float(number)
print(the_decimal(decimal_number))