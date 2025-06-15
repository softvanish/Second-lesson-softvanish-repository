# Очистити текст від html-тегів

import re
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):

    pattern = r'>\s*([а-щА-ЩЬьЮюЯяЇїІіЄєҐґa-zA-ZА-Яа-я\s.,;:!?—–-]+)\s*<'

    result = []

    with codecs.open(html_file, 'r', 'utf-8') as file:
        for line in file:
            text = re.findall(pattern, line)
            result.extend(text)

    with codecs.open("clean.txt", 'w', 'utf-8') as result_file:
        for word in result:
            result_file.write(word + "\n")


delete_html_tags("draft.html")
print("Ok")






