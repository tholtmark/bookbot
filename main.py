from string import ascii_lowercase

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
    #this takes the return of function word_counter and prints it via variable word_count
    word_count = word_counter(file_contents)
        
    character_totals = character_counter(file_contents)
    sorted_chars = sort_dict_descending(character_totals)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for char_dict in sorted_chars:
        print(f"The '{char_dict['character']}' character was found {char_dict['amount']} times")
    print("--- End report ---")
   
def word_counter(file_contents):
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

def sort_dict_descending(character_totals):
    # create an empty list to store our dictionaries
    char_list = []
    
    # iterate through the original dictionary
    for char, count in character_totals.items():
        # create a new dictionary for each character and append it to the list
        char_dict = {"character": char, "amount": count}
        char_list.append(char_dict)
    
    # sort the list using the sort_on function as shown in the hint
    def sort_on(dict):
        return dict["amount"]
        
    char_list.sort(reverse=True, key=sort_on)
    return char_list
      
 # This line tells Python to run main() when this file is run directly
if __name__ == "__main__":
    main() 