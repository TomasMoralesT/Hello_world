def get_book_text(path):
    with open(path) as f:
        return f.read()
#import text from book

def get_num_words(text):
    words = text.split()
    return len(words)

#Number of words in text

def lower_text(text):
    words = text.split()
    full_text = ''.join(words)
    lowered_words = full_text.lower()
    return lowered_words
#change text all to lowercase and merge words in one string

def main():
    letters = {}
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    glued_words = lower_text(text)
    
    for letter in glued_words:
        if letter.isalpha():
            if letter in letters:
                letters[letter] +=1
            else:
                letters[letter] = 1
    
    char_list = transform_dictionary(letters)

    char_list.sort(key=sort_on, reverse=True)   

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def transform_dictionary(letters):
    char_list = []

    for char, count in letters.items():
        char_dict = {'char': char, 'num': count}
        char_list.append(char_dict)
           
    return char_list

def sort_on(dictionary):
    return dictionary['num']



main()