
import re

def is_phrase_isogram(phrases):
    
    s = re.findall('[a-zA-Z0-9]',phrases)
    res = []
    for element in s:
        if element not in res:
            res.append(element)

    if(len(res) == len(s)):
        return True
    return False

phrase = input('Insert the phrase: ')
if is_phrase_isogram(phrase):
    print(phrase + ' is an isogram')
else:
    print(phrase + ' is NOT an isogram')
