# Question 6: Count Vowels

# Write a program that counts the number of vowels in a sentence

VOWELS =('a', 'e',  'i', 'o', 'u') # a tuple of vowels

sentence =input("Enter a sentence: ") # input prompt

# count unique vowel occurence in a string
vowels_count =len(set([*filter(lambda x: True if x.lower() in VOWELS else False, sentence)])) 

print(vowels_count) # display the result