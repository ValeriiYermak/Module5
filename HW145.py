import re


import re
def find_all_phones(text):
    result = []
    raw_result = re.findall(r"\+380\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}", text)
    for item in raw_result:
        item = item[:17]
        result.append(item)
    return result