
#This is based on MIT's Intro to Computer Science with Python
# The Popular Game called Ghost
import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!


def current_word_frag(word_frag, wordlist):
     for words in wordlist:
        if word_frag in words and word_frag[0] == words[0]:
            if word_frag in words and word_frag == words[:]:
                return False
            else:
                return True

def is_three_letter_word(word_frag, wordlist):
    for words in wordlist:
        if word_frag in words and word_frag[0] == words[0]:
            if word_frag in words and word_frag == words[:]:
                if word_frag in words and len(word_frag) == 3:
                    return True




    
        

print 
print 'Welcome to Ghost!'

print

game_over = False

word_frag = ''

print 'Player 1 Starts!'

while game_over == False:

    print 'Current Word Fragment: ', string.upper(word_frag)

    player1 = raw_input('Player 1 says letter: ')

    word_frag = word_frag + player1

    if current_word_frag(word_frag, wordlist) or is_three_letter_word(word_frag, wordlist):
        print 'Current Word Fragment: ', string.upper(word_frag)
    else:
        print 'Player 2 wins!!'
        game_over = True

    player2 = raw_input('Player 2 says letter: ')

    word_frag = word_frag + player2

    if current_word_frag(word_frag, wordlist) or is_three_letter_word(word_frag, wordlist):
        print 'Current Word Fragment: ', string.upper(word_frag)
    else:
        print 'Player 1 wins!!'
        game_over = True

##for words in wordlist:
##    if 'S' in words and 'S' == words[0]:
##        print words

    






