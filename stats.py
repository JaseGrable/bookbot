def count_num_words(string):
    word_list = string.split()
    return len(word_list)

def count_characters(string):
   characters = {}
   lowercase_string = string.lower()
   
   for char in lowercase_string:
       if char in characters:       
           characters[char] += 1
       else:
           characters[char] = 1
   return characters

def sorted_characters(char_counts):
    char_list = []
    for char, count in char_counts.items():  # Use the correct parameter name
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list
