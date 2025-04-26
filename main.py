from stats import word_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    x = get_book_text("books/frankenstein.txt")
    print(x)
    y = word_count(x)
    print(f"{y} words found in the document")

if __name__ == "__main__":
    main()