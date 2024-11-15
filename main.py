def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)

    word_count = word_counter(file_contents)
    print(f"The total number of words in this book is: {word_count}")

    
def word_counter(file_contents):
    words = []
    # this splits the string into a list of words
    words = file_contents.split()

    # this counts the number of words in the list and returns the value
    total_words = len(words)
    return total_words

# This line tells Python to run main() when this file is run directly
if __name__ == "__main__":
    main() 