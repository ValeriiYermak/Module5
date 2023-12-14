import re


def find_all_words(text, word):
    
    find_list = []                                          # Створюємо новий список
    result = re.findall(word, text, flags=re.IGNORECASE)    # Робимо пошук та приводимо до єдиної літерації
    for word in text:                                       # ітеруємо текст по відношенню до слова
        if word !='' and result == None:                    # В разі коли слово не дорівнює пустому значенні і результат не заданий
            find_list = find_list.append(word)              # добавляємо слово в кінець нового списку
        return(result)                                      # повертаємо список                               # повертаємо новий список
    

# obj = findall(r"\w*", "Fly in the sky.")
# print(obj)

# for word in obj:
#   obj = search(r"[aeiou]",word)
#   if word!='' and obj==None:
#     print(word)


# def find_all_words(text, word):
#     find_dict = {
#         'result' : [],
#         'first_index': [],
#         'last_index': [],
#         'search_string': [],
#         'string': []
#     }
#     search_var = re.findall(word, text)
#     flag = re.IGNORECASE
#     if word in text:
#         find_dict['result'] = True
#         find_dict['first_index'] = search_var.start()
#         find_dict['last_index'] = search_var.end()
#         find_dict['search_string'] = word
#         find_dict['string'] = text
#     else:
#         find_dict['result'] = False
#         find_dict['first_index'] = None
#         find_dict['last_index'] = None
#         find_dict['search_string'] = word
#         find_dict['string'] = text
#     return(find_dict)




# import re
# print (re.search('bush', 'BuSh', re.IGNORECASE))
# print (re.match('bush', 'BuSh', re.IGNORECASE))
# print (re.sub('bush', 'xxxx', 'Bushmeat', flags=re.IGNORECASE)