from stats import count_words, count_each_character, sort_character_counts, total_characters
import sys

# used to calculate the length of the separators in the output
# maintain a consistent length
total_separator_length: int = 33

def separator_length(word):
    return (total_separator_length - total_characters(count_each_character(word))) // 2

# opens the file at the given path and returns its contents as a string
def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()


def main():
    # check if the user provided a file path as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = count_words(book_text)
    character_counts = count_each_character(book_text)
    sorted_character_counts = sort_character_counts(character_counts)

    # print the results in a formatted way
    print(f"{'=' * separator_length('BOOKBOT')} BOOKBOT {'=' * separator_length('BOOKBOT')}")
    print(f"Analyzing book found at {file_path}...")
    print(f"{'-' * separator_length('Word Count')} Word Count {'-' * separator_length('Word Count')}")
    print(f"Found {word_count} total words.")
    print(f"{'-' * separator_length('Character Count')} Character Count {'-' * separator_length('Character Count')}")

# print the character counts in a formatted way, only showing alphabetic characters
    for character in sorted_character_counts:
        if character['char'].isalpha():
            print(f"{character['char']}: {character['num']}")
    print(f"{'=' * separator_length('END')} END {'=' * separator_length('END')}")



main()