import sys
from stats import num_of_words, num_of_chars, sort_on, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    word_count = num_of_words(book)
    char_data = num_of_chars(book)
    ordered_data = sorted_list(char_data)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for dictionary in ordered_data:
        print(f"{dictionary["char"]}: {dictionary["num"]}")

    print("============= END ===============")

main()