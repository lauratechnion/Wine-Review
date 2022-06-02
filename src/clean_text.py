import string
import re as regex

specialChars = ''.join([",", ":", "\"", "=", "&", ";", "%", "$","@", "%", "^", "*", "(", ")", "{", "}",'–','“', '”'
                      "[", "]", "|", "/", "\\", ">", "<", "-","!", "?", ".", "'","--", "---", "#", '‘', '’', '…'])  
space_chars = ['.',',',';', '&', '?','!']

def remove_by_regex(texts, regexp):
    return texts.replace(regexp, "")

def remove_special_chars(texts): 
    return texts.apply(lambda text: ''.join([c for c in text if c not in specialChars]))

def remove_numbers(texts):
    return remove_by_regex(texts, regex.compile(r"\s?[0-9]+\.?[0-9]*"))

def add_spaces(texts):
    def add_spaces_int(text):
        for char in space_chars:
            text = text.replace(char, char + ' ')
        return text
    return texts.apply(lambda text: add_spaces_int(text))

def leave_language_only(texts):
    for f in [add_spaces, remove_numbers, remove_special_chars]:
        texts = f(texts)
    return texts