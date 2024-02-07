# Question 3: Power of Two

# Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(number:int)->bool:

    """
    Checks whether an interger is a power of 2

    i.e returns true if 2^x =number. where x <number

    @params: {number:int} - the integer to check if its a power of 2
    @returns {bool} - whether the number provided is a power of 2
    """
    
    for e in range(number +1): # iterate through values between 0 and the number under investigation

        if 2 **e ==number: # check if 2 raised to a value, e is equivalent to the number of interest
            return True

    return False

if __name__ =='__main__': # function use is within this script

    number =input("Enter a an integer number: ") # prompt user for an integer number

    if number.isdigit(): # ensure user provided an integer

        number =int(number) # cast the value to integer

        result =is_power_of_two(number) # check if it's a power of 2

        print(result) # display result

    else: # user input is not an integer

        print("The input value must be an interger")