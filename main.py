def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = chars_dict_to_sorted_list(chars_dict)

    # prints report
    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document\n")
    for item in chars_list:
        if item["name"].isalpha():
            print(f"The '{item["name"]}' character was found {item["count"]} times")
    print("--- End report ---")

# opens the book
def get_book_text(path):
    with open(path) as f:
        return f.read()

# return number of words in text
def get_num_words(text):
    words = text.split()
    return len(words)

# returns a dictionary of the count of all characters used in text, coverting everything to lowercase
def get_chars_dict(text):
    chars_dict = {}

    lower_case = text.lower()

    for letter in lower_case:
        if letter not in chars_dict:
            chars_dict[letter] = 0
        chars_dict[letter] += 1

    return chars_dict

# tells the sort function to sort by the count of characters
def sort_on(dict):
    return dict["count"]

# converts a character dictionary into a list of dictionaries and sorts based on the count of characters
def chars_dict_to_sorted_list(dict):
    chars_list = []

    for item in dict:
        chars_list.append({"name": item, "count": dict[item]})

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list


main()