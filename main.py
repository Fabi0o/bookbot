from stats import count_words, count_letters, sort_dicts
import sys

def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text = f.read()

    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    letters = sort_dicts(count_letters(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for letter in letters:
        print(f"{letter["char"]}: {letter["num"]}")
    
    print("============= END ===============")


main()
