def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
   
    new_dict_phones = {"UA": [],
                       "JP": [],
                       "TW": [],
                       "SG": []}
       
    if len(list_phones) == 0:
        return new_dict_phones      
    for phone in list_phones:
        sanitize_phone = sanitize_phone_number(phone)
        if sanitize_phone[:2] == '81':
            new_dict_phones["JP"].append(sanitize_phone)
        elif sanitize_phone[:2] == '65':
            new_dict_phones["SG"].append(sanitize_phone)
        elif sanitize_phone[:2] == '88':
            new_dict_phones["TW"].append(sanitize_phone)
        elif sanitize_phone[:2] == '38':
            new_dict_phones["UA"].append(sanitize_phone)
        else:
            new_dict_phones["UA"].append(sanitize_phone)

    return new_dict_phones
    

    # if len(list_phones) == 0:
    #     return new_dict_phones
    # for phon in list_phones:
    #     telephone = sanitize_phone_number(phon)
    #     if telephone.startswith("38"):
    #          new_dict_phones.get("UA").append(telephone)
    #     if telephone.startswith("81"):
    #          new_dict_phones.get("JP").append(telephone)
    #     if telephone.startswith("65"):
    #          new_dict_phones.get("SG").append(telephone)
    #     if telephone.startswith("886"):
    #          new_dict_phones.get("TW").append(telephone)
    #     else:
    #         new_dict_phones.get("UA").append(telephone)
    # return new_dict_phones