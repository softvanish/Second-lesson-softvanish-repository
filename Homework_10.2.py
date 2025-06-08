# Знайти перше слово

import re


def first_word(text):

    """ Пошук першого слова """

    '''  
    
    pattern_first_word = r"\s*([A-Za-z\']+)" 
    
    \s* - тут мы пропускаем все возможные пробелы
    () - с помощью скобок мы обьеденяем часть регулярки, чтобы потом её вернуть в return 
    [] - создаем допустимые символы для слова
    A-Za-z\' - пишем что все допустимые символы это англ алфавит и апостроф
    + - делаем так, чтобы пайтон захватил все слово, а не букву
    
    '''

    pattern_first_word = r"\s*([A-Za-z\']+)"

    word = re.search(pattern_first_word, text)

    if word:
        return word.group(1)

#########################################


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
