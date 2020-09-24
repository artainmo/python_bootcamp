import string

def text_analyzer(text=None):
    """Summary or Description of the Function
    Verifies number of chars, upper, lower, spaces and punctuation marks

    Parameters:
    argument1 (str): text

    Returns:
    void
    """

    if text == None:
        text = input("What is the text to analyse?\n >> ")
    characters = len(text)
    upper = 0
    space = 0
    lower = 0
    punctuations = 0
    for char in text:
        if char.islower() == True:
            lower += 1
        elif char.isupper() == True:
            upper += 1
        elif char.isspace() == True:
            space += 1
        elif char in string.punctuation:
            punctuations += 1
    print("The text contains", characters, "characters:\n")
    print("-", upper, "upper letters\n")
    print("-", lower, "lower letters\n")
    print("-", punctuations, "punctuation marks\n")
    print("-", space, "spaces")
