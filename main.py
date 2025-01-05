def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words was found in the document.\n")
    char_count = char_number(text)
    for x in char_count:
        print(f"The '{x['char']}' character was found: {x['count']} times")
    print('--- End report ---')

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(mytext):
    words = mytext.split()
    #print(words)
    return len(words)

def char_number(mytext):
    non_alpha_lower = ''.join([c for c in mytext if c.isalpha()]).lower()
    words_dict_no = {}
    for char in non_alpha_lower:
        if char in words_dict_no:
            words_dict_no[char] += 1
        else:
            words_dict_no[char] = 1
    list_of_dicts = [{'char': k, 'count': v} for k, v in words_dict_no.items()]
    list_of_dicts.sort(reverse=True, key=lambda x: x['count'])
    return list_of_dicts


main()