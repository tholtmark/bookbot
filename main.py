from string import ascii_lowercase

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
    # print(file_contents)

    word_count = word_counter(file_contents)
    print(f"The total number of words in this book is: {word_count}")
    character_totals = character_counter(file_contents)
    print(character_totals)

    
def word_counter(file_contents):
    words = []
    # this splits the string into a list of words
    words = file_contents.split()

    # this counts the number of words in the list and returns the value
    total_words = len(words)
    return total_words

def character_counter(file_contents):
    character_count = {}
    for i in file_contents:
        if i in ascii_lowercase:
            character_count[i] = character_count.get(i, 0) + 1
    return character_count


# This line tells Python to run main() when this file is run directly
if __name__ == "__main__":
    main() 