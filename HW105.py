import re


def find_word(text, word):
    find_dict = {
        'result' : [],
        'first_index': [],
        'last_index': [],
        'search_string': [],
        'string': []
    }
    search_var = re.search(word, text)
    if word in text:
        find_dict['result'] = True
        find_dict['first_index'] = search_var.start()
        find_dict['last_index'] = search_var.end()
        find_dict['search_string'] = word
        find_dict['string'] = text
    else:
        find_dict['result'] = False
        find_dict['first_index'] = None
        find_dict['last_index'] = None
        find_dict['search_string'] = word
        find_dict['string'] = text
    return(find_dict)

        