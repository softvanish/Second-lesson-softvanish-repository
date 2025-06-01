# Паліандром

import string
punctuation = list(string.punctuation)

def is_palindrome(text):
    text = text.lower()
    text_list = list(text)                                     # Создаём пустой лист и приводим всё в нижний регистр
    i = 0

    while i < len(text_list):
        if text_list[i] in punctuation or text_list[i] == " ":  # Тут убираем все знаки из punctuation и пробелы
            text_list.pop(i)
        else:
            i += 1

    if text_list[::-1] == text_list:                             # Сравниваем
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
