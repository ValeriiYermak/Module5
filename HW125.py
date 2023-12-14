import re


# def replace_spam_words(text, spam_words):
    
#     result = ""
#     text = text.lower().replace(",", "").replace(".", "")
#     arr_text = text.split(" ")
#     for word in arr_text:
#         for spam in spam_words:
#             if spam == word:
#                     result = re.sub(spam, "*" * len(spam), text, flags = re.IGNORECASE)
#         return result
        


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, '*'*len(word), text, flags=re.IGNORECASE)
    return text