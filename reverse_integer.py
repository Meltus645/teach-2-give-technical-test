# Question 5: Reverse Integer

# Write a program that takes an integer as input and returns an integer with reversed digit ordering

def reverse_integer(number: int)->int:

    """
    Accepts an integer and reverses the order of digits in the integer and then returns the new integer

    i.e 500 => 5, -56 => -65

    @params: number: int - User input
    @returns: reversed_number: int - number reversed
    """

    number_str =str(abs(number)) # cast the absolute value of the number to a str

    reversed_number =number_str[::-1] # reverse the elements of the str
    if number <0: reversed_number =f"-{reversed_number}" # if number is negative add the negative sign back

    return int(reversed_number) # cast the reverse string as an int


if __name__ =='__main__':

    user_input =input("Enter an integer: ") # get user input

    if user_input.isdigit() or (user_input[0] =='-' and user_input[1:].isdigit()): # check if user input is an integer

        number =int(user_input) # cast to integer

        result =reverse_integer(number) # reverse the user input

        print(result) # display result

    else: # user input was not an integer

        print("Prompt expected an integer value!")