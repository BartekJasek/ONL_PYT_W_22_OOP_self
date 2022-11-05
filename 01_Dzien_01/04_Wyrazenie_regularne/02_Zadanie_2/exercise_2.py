import re


with open('text.txt', 'r') as fin:
    text_to_search = fin.read()
    #  Tutaj umieść swoje rozwiązanie!
    word_autor = re.findall(r'[Aa]utor', text_to_search)
    print(word_autor)
    number_sequence = re.findall(r'\d+', text_to_search)
    print(number_sequence)
    dot = re.findall(r'[a-zA-Z]*[.]', text_to_search)
    print(dot)
    word_polski = re.findall(r'[Pp]olski', text_to_search)
    print(word_polski)
