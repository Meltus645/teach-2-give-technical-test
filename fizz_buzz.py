# Question 1: FizzBuzz

# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print "FizzBuzz".

for num in range(0, 100):

    num =num +1
    if (num %5 ==0) and (num %3 ==0): # check if num is a multiple of both 5 and 3
        print('FizzBuzz')

    elif num %5 ==0: # check num is a multiple of 5 only
        print('Buzz')

    elif num %3 ==0: # check num is a multiple of 3 only
        print('Fizz')
        
    else: # otherwise
        print(num)