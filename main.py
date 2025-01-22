import string

def main():
    fpath = "books/frankenstein.txt"
    file_contents = get_book_text(fpath)
    char_count = count_chars(file_contents)

    char_list = list(char_count.items())
    char_list.sort(reverse=True, key=lambda x: x[1])

    print(f"--- Begin report of {fpath}")
    print(f"{count_words(file_contents)} words found in the document")
    print()
    #for c in char_count.keys():
    #    print(f"The '{c}' character was found {char_count[c]} times")
    for c in char_list:
        print(f"The '{c[0]}' character was found {c[1]} times")
    print("--- End report ---")

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

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()