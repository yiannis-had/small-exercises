import string

alphabet = {letter: str(index) for index, letter in enumerate(string.ascii_lowercase, start=1)} 

def replaceLetterWithPosition(string):
    string = string.lower()
    numbers = [alphabet[letter] for letter in string if letter in alphabet]
    return ' '.join(numbers)

string = replaceLetterWithPosition("This NETbuilder assessment is way too easy.")
print(string)