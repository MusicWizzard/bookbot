def word_count(text):
    string = text.split()
    words = len(string)
    return words
def how_many_chars(text):
    ac_text = text.lower()
    dictionary = {}
    for i in ac_text:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary
def chars_dict_to_sorted_list(char_dict):
    empty_list = []
    for i, u in char_dict.items():
        empty_list.append({"char": i, "num": u})
    empty_list.sort(reverse=True, key=lambda x:x["num"])
    return empty_list