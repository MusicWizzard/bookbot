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