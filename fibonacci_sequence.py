# Question 2: Fibonacci Sequence

# Write a program to generate the Fibonacci sequence up to 100

limit =100 # the first <limit> numbers

sequence = [] # empty list to store the sewquence

prev, curr =(0, 1) # set the initial values of the sequence

for _ in range(limit +1): # loop through the first <limit> numbers

    if prev >limit: break # exit loop if the previous value exceeds the <limit>

    sequence.append(prev) # add values to the sequence

    prev, curr =(curr, prev + curr) # update the values

print(sequence) # display the sequence