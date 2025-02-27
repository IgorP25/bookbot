import string

def count_chars(text):
    #chars = set()
    char_count = {}

    #for c in text.casefold():
        #chars.add(c)
    #for c in chars:
    for c in string.ascii_lowercase:
        char_count[c] = text.casefold().count(c)
    return char_count

def count_words(text):
    word_count = text.split()
    return len(word_count)