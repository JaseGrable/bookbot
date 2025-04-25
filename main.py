from stats import count_num_words, count_characters, sorted_characters

import sys  

def get_book_text(filepath): 
    with open(filepath) as f: 
        return f.read()


    
   

def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    book_text = get_book_text(filepath)
    word_count = count_num_words(book_text)  
    print(f"Found {word_count} total words")
    
    character_counts = count_characters(book_text) 
    sorted_counts = sorted_characters(character_counts)
    print("\n--------- Character Count -------\n")
    for entry in sorted_counts: 
        char = entry["char"]
        count = entry["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============ BOOKBOT ============")
main()







