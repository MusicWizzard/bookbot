from stats import word_count, how_many_chars, chars_dict_to_sorted_list
import sys
def print_report(filepath, word_count, how_many_chars):
    sorted_chars = chars_dict_to_sorted_list(how_many_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    filepath = sys.argv[1]
    x = get_book_text(filepath)
    y = word_count(x)
    z = how_many_chars(x)
    print_report(filepath, y, z)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()