def real_len(text):
    char_count = 0
    for char in text:
        if char not in ['\n', '\f', '\r', '\t', '\v']:
            char_count += 1
    return char_count