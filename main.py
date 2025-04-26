from stats import word_count, how_many_chars
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    x = get_book_text("books/frankenstein.txt")
    print(x)
    y = word_count(x)
    print(f"{y} words found in the document")
    z = how_many_chars(x)
    print(z)

if __name__ == "__main__":
    main()