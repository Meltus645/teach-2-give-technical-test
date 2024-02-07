# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100

sequence = []
limit =100
prev, curr =(0, 1)

for _ in range(limit):
    if prev >=limit: break
    sequence.append(prev)
    prev, curr =(curr, prev + curr)

print(sequence)