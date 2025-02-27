import sys
from stats import count_chars, count_words

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    fpath = sys.argv[1]
    file_contents = get_book_text(fpath)
    char_count = count_chars(file_contents)

    char_list = list(char_count.items())
    char_list.sort(reverse=True, key=lambda x: x[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}...")
    print("----------- Word Count ----------")
    # print(f"{count_words(file_contents)} words found in the document")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
    for c in char_list:
        print(f"{c[0]}: {c[1]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()