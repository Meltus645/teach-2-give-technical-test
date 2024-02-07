# Question 4: Capitalize Word

# Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.

def capitalize_words(text:str)->str:

    """ Accepts a string and returns a new instance of the string in title case

    @params: {text:str} - The string to convert to title case
    @returns: {str} - A new string in title case
    """
    
    words =[word.capitalize() for word in text.split(' ')] # store capitalized words

    return ' '.join(words) # join words into a string

if __name__ =='__main__':

    text =input("Enter text: ") # input text to transform

    capitalized_text =capitalize_words(text =text)  # title case the text entered

    print(capitalized_text) # display the results