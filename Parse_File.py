#	Author: Kenneth Murry
#	CptS 422 
#	Objective: A utility method that reads a file word by word

import itertools
import sys

def read_words(mfile):
    byte_stream = itertools.groupby(
        itertools.takewhile(lambda c: bool(c),
            map(mfile.read,
                itertools.repeat(1))), str.isspace)

    return ("".join(group) for pred, group in byte_stream if not pred)

def parse_file(file_path, start_word, end_word):
    found = False
    list = []

    # If we are looking for the description the start_word will
    # be passed in as the empty string '' and end_word will be 'STATES:'
    if start_word == '' and end_word == 'STATES:':
        found = True
    try:
        with open(file_path, 'r') as f:
            for word in read_words(f):
                if word.upper() == end_word:
                    found = False
                    break
                if found == True and word.upper() != end_word:
                    list.append(word)
                if word.upper() == start_word:
                    found = True
        f.close()
        return list
    except IOError:
        list = 'Error'
        return list

# Example of how to use the method parse_file to get Final States
# Uncomment code under to see a test
#final = []
#final = parse_file('pda.de', 'FINAL_STATES:', '')
#print(final)

# Example of how to use the method parse_file
# Uncomment code under to see a test
#states = []
#states = parse_file('pda.def', 'STATES:', 'INPUT_ALPHABET:')
#print(states)

# Example of how to use the method parse_file to get description
# Uncomment code under to see a test
#description = []
#description = parse_file('pda.def', '', 'STATES:')
#print(' '.join(description)) #Display the list without the list format

# Example of how to use the method read_words
# Uncomment code under to see a test
#found = False
#states = []
#with open('pda.def', 'r') as f:
#    for word in read_words(f):
#        if word == 'INPUT_ALPHABET:':
#            found = False
#        if found == True and word != 'INPUT_ALPHABET:':
#            states.append(word)
#        if word == 'STATES:':
#            found = True
#
#    print(states)
#
#    f.close()

