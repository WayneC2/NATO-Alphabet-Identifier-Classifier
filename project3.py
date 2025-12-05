'''
Project 3 - NATO Alphabet - Fall 2025
Wayne C

This program reads a NATO alphabet mapping from alphabet.txt and then
reads identifiers from identifiers.txt. It classifies each identifier as
a TAG, VIN, or INVALID based only on its length, then prints the identifier
and (if valid) spells it out using the NATO alphabet words. At the end,
it prints the total number of valid and invalid identifiers found.

I have neither given nor received unauthorized assistance on this assignment.
Signed: Wayne C
'''

def get_dictionary():
    '''
    Reads alphabet.txt and returns a dictionary mapping characters to NATO words.
    Adds entries for space (' ') as 'Space' and dash ('-') as 'Dash'.
    Parameters: none
    Return: dictionary of character -> code word
    '''
    alphabet_dict = {}

    infile = open('alphabet.txt', 'r')
    for line in infile:
        line = line.strip()
        if line != "":
            parts = line.split()
            key = parts[0]
            value = parts[1]
            alphabet_dict[key] = value
    infile.close()

    # Add required special characters
    alphabet_dict[' '] = 'Space'
    alphabet_dict['-'] = 'Dash'

    return alphabet_dict


def categorize_identifier(identifier):
    '''
    Determines whether an identifier is a TAG, VIN, or INVALID.
    TAG: length 5–8 characters
    VIN: length 17 characters
    Parameters:
        identifier - the identifier to categorize (string)
    Return:
        'TAG', 'VIN', or 'INVALID'
    '''
    length = len(identifier)

    if 5 <= length <= 8:
        return 'TAG'
    elif length == 17:
        return 'VIN'
    else:
        return 'INVALID'


def get_spelling(alphabet_dict, identifier):
    '''
    Converts an identifier into its NATO-coded spelling.
    Each character is converted using the alphabet_dict mapping.
    Parameters:
        alphabet_dict - the dictionary of character -> NATO word
        identifier - the string to spell out
    Return:
        NATO spelling as a single string (words separated by spaces)
    '''
    words = []
    for ch in identifier:
        if ch in alphabet_dict:
            words.append(alphabet_dict[ch])
    return " ".join(words)


def main():
    '''
    Driver function. Reads alphabet, processes identifiers, prints results.
    Parameters: none
    Return: none
    '''
    alphabet_dict = get_dictionary()

    infile = open('identifiers.txt', 'r')

    valid_count = 0
    invalid_count = 0

    for line in infile:
        identifier = line.strip().upper()

        category = categorize_identifier(identifier)

        if category == 'INVALID':
            print("INVALID:", identifier)
            invalid_count += 1
        else:
            print(category + ":", identifier)
            spelling = get_spelling(alphabet_dict, identifier)
            print(spelling)
            valid_count += 1

        print()  # blank line after each entry

    infile.close()

    print("Number of valid identifiers:", valid_count)
    print("Number of invalid identifiers:", invalid_count)


if __name__ == '__main__':
    main()