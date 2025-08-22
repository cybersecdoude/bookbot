def num_of_words(book_text):
    return len(book_text.split())

def num_of_chars(book_text):
    data = {}
    for char in book_text:
        char = char.lower()
        if char in data:
            data[char] += 1
        else:
            data[char] = 1
    return data

def sort_on(items):
    return items["num"]

def sorted_list(char_counts):
    data = []
    for key, value in char_counts.items():
        if key.isalpha():
            data.append(
                {
                    "char": key,
                    "num": value
                }
            )
    data.sort(reverse=True, key=sort_on)
    return data