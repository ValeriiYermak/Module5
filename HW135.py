import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]\S+[@]\w\w+[.]\w\w+", text)
    return result