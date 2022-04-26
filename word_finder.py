import re
from string import ascii_lowercase


def check_word(word, allowed_letters):
    """
    Check if a word meets the critera for the spelling bee game:
        * The word may only contain the allowed_letters.
        * The first letter in allowed_letters is the key letter. The word
          must contain it.
        * The words must be four characters or more in length.
    """
    key_letter = allowed_letters[0] # first letter is "key." it must be contained
    bad_letters = re.sub(f'[{allowed_letters}]', '', ascii_lowercase) # get all un-allowed letters
    
    word = word.lower()
    if len(word) < 4:
        return False 
    if key_letter not in word:
        return False
    if re.search(f'[{bad_letters}]', word):           
        return False
    
    return True

def word_finder(allowed_letters):
    """
    Return a list of words that meet the critera for the spelling bee game.
    """

    with open('data/norvig_word_list.txt') as f: 
        # file downloaded from http://norvig.com/ngrams/word.list
        word_list = [word.strip() for word in f.readlines()]

    good_words = [w for w in word_list if check_word(w, allowed_letters)]
    good_words.sort(key=len)

    return good_words


def find_pangrams(good_words, n=7):
    """Return a list of pangrams (ie words containing all allowed letters)
        from a list of words. """

    # there are 7 letters in the game, any word with 7 unique letters is a pangram
    return [w for w in good_words if len(set(w)) == n]